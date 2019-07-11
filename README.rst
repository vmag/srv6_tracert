srv6\_tracert
=============

Usage
-----

::

    usage: srv6_traceroute.py [-h] (-d DESTINATION | -f DESTINATION_FILE)
                              [-c COUNT] [-s PACKETSIZE] [-t TIMEOUT]
                              [-v VERBOSITY]

    SRv6 traceroute script

    optional arguments:
      -h, --help            show this help message and exit
      -d DESTINATION, --destination DESTINATION
                            Destination host IPv6
      -f DESTINATION_FILE, --destination_file DESTINATION_FILE
                            File with destination hosts IPv6
      -c COUNT, --count COUNT
                            Count of random IPv6 SR hops
      -s PACKETSIZE, --packetsize PACKETSIZE
                            ICMP echo packet data size
      -t TIMEOUT, --timeout TIMEOUT
                            Scapy packet timeout
      -v VERBOSITY, --verbosity VERBOSITY
                            Scapy verbosity

Example of DESTINATION\_FILE is in the file ``hosts.yml.example``.

Sample output
-------------

Single traceroute
~~~~~~~~~~~~~~~~~

::

    -> srv6_traceroute.py -d dead:beef:ca1f
    ======= Starting ICMP (packet size: 8) traceroute to dead:beef:ca1f =======
    ======= Starting SRv6 (packet size: 8) traceroute to dead:beef:ca1f =======
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+
    | TTL |             ASN             |         ICMP dst        |          SR dst         |      Latency       |
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+
    |  1  |              -              |            -            |            -            |         -          |
    |  2  |              -              |            -            |            -            |         -          |
    |  3  | AS-CHOOPA - Choopa, LLC, US | 2001:19f0:5000::a48:131 |            -            | 9.755134582519531  |
    |  4  |         AMS-IX1, NL         | 2001:7f8:1::a502:4940:1 | 2001:7f8:1::a502:4940:1 | 44.83842849731445  |
    |  5  |        HETZNER-AS, DE       |    2a01:4f8:0:3::11d    |    2a01:4f8:0:3::11d    | 24.158716201782227 |
    |  6  |        HETZNER-AS, DE       |     2a01:4f8:0:3::f9    |     2a01:4f8:0:3::f9    | 27.796506881713867 |
    |  7  |        HETZNER-AS, DE       |  2a01:4f8:0:e0c0::a002  |  2a01:4f8:0:e0c0::a002  | 33.812522888183594 |
    |  8  |              -              |            -            |            -            |         -          |
    |  9  |        HETZNER-AS, DE       |  2a01:4f8:0:e0c0::1c16  |  2a01:4f8:0:e0c0::1c16  | 20.31564712524414  |
    |  10 |              -              |            -            |            -            |         -          |
    |  11 |        HETZNER-AS, DE       |      dead:beef:ca1f     |      dead:beef:ca1f     | 17.747879028320312 |
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+

Multi destination traceroute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    -> srv6_traceroute.py -f hosts.yml
    Performing traceroute on server host1 (dead:beef:ca1f)
    ======= Starting ICMP (packet size: 8) traceroute to dead:beef:ca1f =======
    ======= Starting SRv6 (packet size: 8) traceroute to dead:beef:ca1f =======
    Results of traceroute to server host1 (dead:beef:ca1f)
    +-----+----------------+-------------------------+-------------------------+--------------------+
    | TTL |      ASN       |         ICMP dst        |          SR dst         |      Latency       |
    +-----+----------------+-------------------------+-------------------------+--------------------+
    |  1  |       -        |            -            |            -            |         -          |
    |  2  |       -        |            -            |            -            |         -          |
    |  3  |       -        |            -            |            -            |         -          |
    |  4  |  AMS-IX1, NL   | 2001:7f8:1::a502:4940:1 | 2001:7f8:1::a502:4940:1 | 7.732629776000977  |
    |  5  | HETZNER-AS, DE |    2a01:4f8:0:3::11d    |    2a01:4f8:0:3::11d    | 14.463424682617188 |
    |  6  | HETZNER-AS, DE |     2a01:4f8:0:3::f9    |     2a01:4f8:0:3::f9    | 18.020153045654297 |
    |  7  | HETZNER-AS, DE |  2a01:4f8:0:e0c0::a002  |  2a01:4f8:0:e0c0::a002  | 17.49587059020996  |
    |  8  |       -        |            -            |            -            |         -          |
    |  9  | HETZNER-AS, DE |  2a01:4f8:0:e0c0::1c16  |  2a01:4f8:0:e0c0::1c16  | 17.79937744140625  |
    |  10 |       -        |            -            |            -            |         -          |
    |  11 | HETZNER-AS, DE |     dead:beef:ca1f      |      dead:beef:ca1f     | 16.185998916625977 |
    +-----+----------------+-------------------------+-------------------------+--------------------+
    Performing traceroute on server host2 (1d1e:f001)
    ======= Starting ICMP (packet size: 8) traceroute to 1d1e:f001 =======
    ======= Starting SRv6 (packet size: 8) traceroute to 1d1e:f001 =======
    Results of traceroute to server host2 (1d1e:f001)
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+
    | TTL |             ASN             |         ICMP dst        |          SR dst         |      Latency       |
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+
    |  1  |              -              |            -            |            -            |         -          |
    |  2  |              -              |            -            |            -            |         -          |
    |  3  | AS-CHOOPA - Choopa, LLC, US | 2001:19f0:5000::a48:131 | 2001:19f0:5000::a48:131 | 22.018909454345703 |
    |  4  |         AMS-IX1, NL         | 2001:7f8:1::a502:4940:1 | 2001:7f8:1::a502:4940:1 | 7.369518280029297  |
    |  5  |        HETZNER-AS, DE       |    2a01:4f8:0:3::11d    |    2a01:4f8:0:3::11d    | 12.90130615234375  |
    |  6  |        HETZNER-AS, DE       |     2a01:4f8:0:3::b2    |     2a01:4f8:0:3::b2    | 18.60523223876953  |
    |  7  |        HETZNER-AS, DE       |     2a01:4f8:0:3::ee    |     2a01:4f8:0:3::ee    | 19.85001564025879  |
    |  8  |        HETZNER-AS, DE       |        1d1e:f001        |        1d1e:f001        | 19.013166427612305 |
    +-----+-----------------------------+-------------------------+-------------------------+--------------------+

Sample when Routing Extension Header is blocked by one of the Tier1 ISPs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    ======= Starting ICMP (packet size: 8) traceroute to dead:beef:cafe =======
    ======= Starting SRv6 (packet size: 8) traceroute to dead:beef:cafe =======
    +-----+----------------------------------------------+------------------------+------------------------+--------------------+
    | TTL |                     ASN                      |        ICMP dst        |         SR dst         |      Latency       |
    +-----+----------------------------------------------+------------------------+------------------------+--------------------+
    |  1  |            LEASEWEB-UK-LON-11, GB            | 2a0d:3001:2100:a002::2 | 2a0d:3001:2100:a002::2 | 81.56800270080566  |
    |  2  |            LEASEWEB-UK-LON-11, GB            |     2a0d:3000::254     |     2a0d:3000::254     | 64.85724449157715  |
    |  3  |          TELIANET Telia Carrier, SE          | 2001:2000:3080:1bbf::1 |           -            | 69.17166709899902  |
    |  4  |          TELIANET Telia Carrier, SE          |  2001:2000:3019:79::1  |           -            | 137.43948936462402 |
    |  5  |          TELIANET Telia Carrier, SE          |  2001:2000:3019:b6::1  |           -            | 145.21098136901855 |
    |  6  |          TELIANET Telia Carrier, SE          |  2001:2000:3019:72::1  |           -            | 167.96255111694336 |
    |  7  |          TELIANET Telia Carrier, SE          |  2001:2000:3018:99::1  |           -            | 170.88818550109863 |
    |  8  |          TELIANET Telia Carrier, SE          | 2001:2000:3080:1b2f::2 |           -            | 138.5951042175293  |
    |  9  | LEASEWEB-USA-WDC-01 - Leaseweb USA, Inc., US |     2607:f5b7::253     |           -            | 140.91253280639648 |
    |  10 | LEASEWEB-USA-WDC-01 - Leaseweb USA, Inc., US |     dead:beef:cafe     |           -            | 144.75488662719727 |
    +-----+----------------------------------------------+------------------------+------------------------+--------------------+

