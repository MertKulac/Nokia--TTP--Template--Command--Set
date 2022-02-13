from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterTunnel-table.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Show_Router_Tunnel-table">
{{Prefix|PREFIX}}   {{Protocol}}       {{Encap_Type}}  {{Tunnel_id}}       {{Preference}}        {{Next_hop|IP}}   {{Metric}}
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)
[appadmin@ryugbz01 Nokia]$ python3 showRouterTunnel-table.py
[
    {
        "Show_Router_Tunnel-table": [
            {
                "Encap_Type": "MPLS",
                "Metric": "0",
                "Next_hop": "10.10.10.121",
                "Preference": "5",
                "Prefix": "10.10.10.121/32",
                "Protocol": "sdp",
                "Tunnel_id": "100"
            },
            {
                "Encap_Type": "MPLS",
                "Metric": "100",
                "Next_hop": "192.168.10.2",
                "Preference": "7",
                "Prefix": "10.10.10.121/32",
                "Protocol": "rsvp",
                "Tunnel_id": "2"
            }
        ]
    }
]
