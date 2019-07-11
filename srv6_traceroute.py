#!/usr/bin/env python3

from argparse import ArgumentParser
from prettytable import PrettyTable
import srv6_tracert
import yaml
import os, sys

def parse_config(filename):    
    with open(filename) as hosts_file:
        return yaml.safe_load(hosts_file)

def print_results(results):
    t = PrettyTable(['TTL', 'ASN', 'ICMP dst', 'SR dst', 'Latency'])

    for ttl, res in results.items():
        t.add_row([ttl, res["ASN"], res["ICMP"], res["SR"], res["latency"]])

    print(t)

def traceroute(destination, sr_hops, packetsize, verbosity, timeout):
    result_table = {}

    print ("======= Starting ICMP (packet size: %i) traceroute to %s =======" % (packetsize, 
                                                                                 destination))

    max_ttl, result_table = srv6_tracert.icmp_traceroute(destination, result_table, 
                                                         packetsize, verbosity, timeout)

    print ("======= Starting SRv6 (packet size: %i) traceroute to %s =======" % (packetsize,
                                                                                 destination))

    result_table = srv6_tracert.srv6_traceroute(destination, result_table, packetsize,
                                                max_ttl, sr_hops, verbosity, timeout)

    return result_table

def multiple_traceroute(destinations, sr_hops, packetsize, verbosity, timeout):
    for destination in destinations:
        print ("Performing traceroute on server %s (%s)" % (destination["name"],
                                                            destination["ipv6"]))
        results = traceroute(destination["ipv6"], sr_hops, packetsize, verbosity, timeout)
        print ("Results of traceroute to server %s (%s)" % (destination["name"],
                                                            destination["ipv6"]))
        print_results(results)
def main():
    parser = ArgumentParser(description="SRv6 traceroute script")
    
    dest_group = parser.add_mutually_exclusive_group(required=True)
    dest_group.add_argument('-d', '--destination', action="store", help="Destination host IPv6")
    dest_group.add_argument('-f', '--destination_file', action="store",
                            help="File with destination hosts IPv6")
    
    parser.add_argument('-c', '--count', action="store", default=3,
                        help="Count of random IPv6 SR hops", required=False, type=int)
    parser.add_argument('-s', '--packetsize', action="store", default=8, 
                        help="ICMP echo packet data size", required=False, type=int)
    parser.add_argument('-t', '--timeout', action="store", default=2,
                        help="Scapy packet timeout", required=False, type=int)
    parser.add_argument('-v', '--verbosity', action="store", default=0,
                        help="Scapy verbosity", required=False, type=int)


    args = parser.parse_args()
    sr_hops = srv6_tracert.generate_hops(args.count)
    
    if args.destination_file is not None:
        dest_file = args.destination_file
        if not os.path.isfile(dest_file):
            print("Destination host file does not exist")
            sys.exit(1)

        destinations = parse_config(dest_file)
        multiple_traceroute(destinations, sr_hops, args.packetsize, args.verbosity, args.timeout)
    else:
        results = traceroute(args.destination, sr_hops, args.packetsize, args.verbosity, 
                             args.timeout)
        print_results(results)
        

if __name__ == "__main__":
    main()
