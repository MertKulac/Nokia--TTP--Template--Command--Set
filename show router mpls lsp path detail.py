from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterMplsLspPathDetail.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="MPLS_Lsp_Path_Detail">
LSP Name         : {{LSP_Name}}
Path LSP ID      : {{Path_LSP_id}}
From             : {{From}}         To                   : {{To}}
Admin State      : {{Admin_State}}                   Oper State           : {{Oper_State}}
Path Name        : {{Path_Name}} Path Type            : {{Path_Type}}
Path Admin       : {{Path_Admin_State}}                   Path Oper            : {{Path_Oper_State}}
Out Interface    : {{Out_Interface}}            Out Label            : {{Out_Label}}
Path Up Time     : {{Path_Uptime_Date}} {{Path_Uptime_Time}}         Path Down Time       : 0d 00:00:00
Retry Limit      : 0                    Retry Timer          : {{Retry_Time}} sec
Neg MTU          : {{Neg_Mtu}}                 Oper MTU             : {{Oper_Mtu}}
Hop Limit        : {{Hop_Limit}}                  Oper HopLimit        : {{Oper_Hop_Limit}}
Hold Priority    : {{Hold_Priority}}                    Oper Hold Priority   : 0
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)

***RESULT***
[appadmin@ryugbz01 Nokia]$ python3 showRouterMplsLspPathDetail.py
[
    {
        "MPLS_Lsp_Path_Detail": [
            {
                "Admin_State": "Up",
                "From": "10.95.204.13",
                "Hold_Priority": "0",
                "Hop_Limit": "255",
                "LSP_Name": "lsp_to_A_CUSTOMER",
                "Neg_Mtu": "1982",
                "Oper_Hop_Limit": "255",
                "Oper_Mtu": "1982",
                "Oper_State": "Up",
                "Out_Interface": "1/1/5:481",
                "Out_Label": "7452",
                "Path_Admin_State": "Up",
                "Path_LSP_id": "14922",
                "Path_Name": "lsp_to_B_CUSTOMER",
                "Path_Oper_State": "Up",
                "Path_Type": "Standby",
                "Path_Uptime_Date": "10d",
                "Path_Uptime_Time": "21:12:42",
                "Retry_Time": "30",
                "To": "10.36.111.104"
            },
            {
                "Admin_State": "Up",
                "From": "156.67.255.16",
                "Hold_Priority": "0",
                "Hop_Limit": "255",
                "LSP_Name": "gla126-1-to-lon38-1",
                "Neg_Mtu": "1500",
                "Oper_Hop_Limit": "255",
                "Oper_Mtu": "1500",
                "Oper_State": "Up",
                "Out_Interface": "lag-50",
                "Out_Label": "34631",
                "Path_Admin_State": "Up",
                "Path_Oper_State": "Up",
                "Path_Uptime_Date": "0d",
                "Path_Uptime_Time": "20:36:35",
                "Retry_Time": "30",
                "To": "78.33.254.104"
            }
        ]
    }
]
