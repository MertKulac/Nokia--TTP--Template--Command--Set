from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterInterface.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="InterfaceTable">
{{InterfaceName}}                   {{AdminState}}       {{OperStatev4}}/{{OperStatev6}}  {{Mode}}    {{Port_SapID}}
   {{IpAddress}}/{{Mask}}                                                  {{PfxState}}
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)

#converting str to json.
result = json.loads(results)

# for i in result[0]["InterfaceTable"]:
#    if "AdminState" in i:
#       print(f'Admin State: {i["AdminState"]}, Interface Name: {i["InterfaceName"]}, OperStatev4:{i["OperStatev4"]}, OperStatev6: {i["OperStatev6"]}, Port_SapID: {i["Port_SapID"]}')
#    elif "IpAddress" in i:
#       print(f'IpAddress: {i["IpAddress"]}, Mask: {i["Mask"]}, PfxState: {i["PfxState"]}')

***RESULT***
[appadmin@ryugbz01 Nokia]$ python3 showRouterInterface.py
[
    {
        "InterfaceTable": [
            {
                "AdminState": "Adm",
                "InterfaceName": "Interface-Name",
                "Mode": "Mode",
                "OperStatev4": "Opr(v4",
                "OperStatev6": "v6)",
                "Port_SapID": "Port/SapId"
            },
            {
                "AdminState": "Up",
                "InterfaceName": "system",
                "IpAddress": "10.10.10.1",
                "Mask": "32",
                "Mode": "Network",
                "OperStatev4": "Up",
                "OperStatev6": "Down",
                "PfxState": "n/a",
                "Port_SapID": "system"
            },
            {
                "AdminState": "Up",
                "InterfaceName": "toSR7-3",
                "IpAddress": "192.168.10.1",
                "Mask": "27",
                "Mode": "Network",
                "OperStatev4": "Up",
                "OperStatev6": "Down",
                "PfxState": "n/a",
                "Port_SapID": "lag-10:900"
            }
        ]
    }
]
