import time, random
from scapy.all import RandString, IPv6, ICMPv6EchoRequest, IPv6ExtHdrSegmentRouting, ICMPv6EchoReply, sr1
from ipwhois import IPWhois

def generate_hops(count, fmt="2001:cafe:beef::%s"):
    return [fmt % hex(random.randint(0, 0xffff))[2:] for i in range(0, count)]

def get_asn_description(ip):
    try:
        asn = IPWhois(ip)
        asn_owner = asn.lookup_rdap(depth=1)
        return asn_owner['asn_description']
    except ipwhois.exceptions.ASNRegistryError:
        return "Unknown ASN"

def icmp_traceroute(destination, result_table, packet_len, verbosity, timeout):
    ttl = 1

    while 1:
        start_time = time.time()
        p = sr1(IPv6(dst=destination, hlim=ttl)/
                ICMPv6EchoRequest(data=RandString(packet_len)), 
                verbose=verbosity, timeout=timeout)

        end_time = time.time()
        latency = ((end_time - start_time) * 1000)
        
        if not ttl in result_table:
            result_table[ttl] = {}

        if p is not None:
            if p[IPv6].src.startswith('fe'):
                result_table[ttl]["ASN"] = "Link local"
            else:
                result_table[ttl]["ASN"] = get_asn_description(p[IPv6].src)
                
            result_table[ttl]["ICMP"] = p[IPv6].src
            if latency > 2000:
                result_table[ttl]["latency"] = "Timeout"
            else:
                result_table[ttl]["latency"] = str(latency)
       
            if ICMPv6EchoReply in p:
                break
        else:
            result_table[ttl]["latency"] = "-"
            result_table[ttl]["ASN"] = "-"
            result_table[ttl]["ICMP"] = "-"
        
        ttl += 1
    
    max_hops = ttl

    return (max_hops, result_table)

def srv6_traceroute(destination, result_table, packet_len, max_ttl, sr_hops, verbosity, timeout):
    ttl = 1

    while ttl <= max_ttl:
        p = sr1(IPv6(dst=destination, hlim=ttl)/IPv6ExtHdrSegmentRouting(addresses=sr_hops)/ICMPv6EchoRequest(data=RandString(packet_len)), 
                     timeout=timeout, verbose=verbosity)
        
        if p is not None:
            if not ttl in result_table:
                result_table[ttl] = {}
            result_table[ttl]["SR"] = p[IPv6].src
        else:
            result_table[ttl]["SR"] = "-"

        ttl += 1

    return result_table
