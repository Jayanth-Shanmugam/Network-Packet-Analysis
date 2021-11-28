#Python script to analyze the traffic captured through wireshark and separate traffic based on application layer protocols
#and display the statistics such as total packets and the average packet length of each application layer protocol.

import pandas as pd

app_protocols = ["HTTP","OCSP","TLSv1.2","TLSv1.3","FTP","DNS","DHCP","FTP-DATA"]

def get_App_count(net_traffic):
    """Function to read traffic file and print the packet count of application layer protocols in the traffic"""
    net_app_traffic = net_traffic[net_traffic.Protocol.isin(app_protocols)]
    nt_app_proto_count = net_app_traffic.groupby('Protocol').Source.count()
    print("Packet count of each application layer protocol in the traffic:- ")
    print("---------------------------------------------------------------------------")
    print(nt_app_proto_count)
    nt_app_proto_count.to_csv("packet_count.csv",encoding = 'utf-8')


def get_Avg_len(net_traffic):
    """Function to read a traffic file, find the average packet size of each application layer protocol and print it"""
    net_app_traffic = net_traffic[net_traffic.Protocol.isin(app_protocols)]
    net_traffic_s=net_app_traffic.groupby('Protocol').Length.sum()
    net_traffic_count = net_app_traffic.groupby('Protocol').Source.count()
    net_traffic_ap=net_traffic_s/net_traffic_count
    print("Average packet length of each application layer protocol in the traffic:- ")
    print("---------------------------------------------------------------------------")
    print(net_traffic_ap)
    net_traffic_ap.to_csv("average_packet_length.csv",encoding = 'utf-8')


net_traffic = pd.read_csv("CN_mini_traffic.csv")
get_App_count(net_traffic)
print('\n')
get_Avg_len(net_traffic)
