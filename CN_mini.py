#Python script to analyze the traffic captured through wireshark and separate traffic based on application layer protocols
#and display the statistics such as total packets and the average packet length of eac application layer protocol.

import pandas as pd

def get_App_count(net_traffic):
    """Function to read traffic file and print the packet count of application layer protocols in the traffic"""
    app_protocols = ["HTTP","OCSP","TLSv1.2","TLSv1.3","FTP","DNS","DHCP","FTP-DATA"]
    net_app_traffic = net_traffic[net_traffic.Protocol.isin(app_protocols)]
    nt_app_proto_count = net_app_traffic.groupby('Protocol').Source.count()
    print(nt_app_proto_count)

net_traffic = pd.read_csv("CN_mini_traffic.csv")
get_App_count(net_traffic)
