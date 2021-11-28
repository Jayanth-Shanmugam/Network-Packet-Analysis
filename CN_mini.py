#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Python script to analyze the traffic captured through wireshark and separate traffic based on application layer protocols
#and display the statistics such as total packets and the average packet length of eac application layer protocol.

import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


def get_App_count(net_traffic):
    """Function to read traffic file and print the packet count of application layer protocols in the traffic"""
    app_protocols = ["HTTP","OCSP","TLSv1.2","TLSv1.3","FTP","DNS","DHCP","FTP-DATA"]
    net_app_traffic = net_traffic[net_traffic.Protocol.isin(app_protocols)]
    nt_app_proto_count = net_app_traffic.groupby('Protocol').Source.count()
    print(nt_app_proto_count)

net_traffic = pd.read_csv("CN_mini_traffic.csv")
app_protocols = ["HTTP","OCSP","TLSv1.2","TLSv1.3","FTP","DNS","DHCP","FTP-DATA"]
get_App_count(net_traffic)


# In[5]:


net_traffic.head()


# In[6]:


net_traffic.Protocol.unique()


# In[7]:


net_traffic.Length.mean()


# In[8]:


net_traffic_g=net_traffic.groupby('Protocol').Source.count()
print(net_traffic_g)


# In[9]:


net_traffic_g.sort_values()


# In[15]:


net_traffic[net_traffic['Protocol']=='TCP'].Length.hist(bins=15)
#Most packets between 0-200 bytes


# In[17]:


net_traffic[net_traffic['Protocol']=='QUIC'].Length.hist(bins=15)
#Most Packets between 1200-1400 bytes


# In[18]:


#Calculate the sum of Length for each protocol and display it in a bar plot.Divide by 1024/1024 to convert bytes to MBytes
net_traffic_s=net_traffic.groupby('Protocol').Length.sum()
net_traffic_s_mb=net_traffic_s/(1024*1024)
net_traffic_s_mb.plot(kind='bar')


# In[20]:


#Print the packet count by protocol
net_traffic_p=net_traffic.groupby('Protocol').Source.count()
net_traffic_p.plot(kind='bar')


# In[21]:


#Divide the total packet size by the packet count to find the average packet size
net_traffic_ap=net_traffic_s/net_traffic_p
net_traffic_ap.plot(kind='bar')


# In[ ]:




