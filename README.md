# Network-Packet-Analysis
Packet analysis is a primary traceback technique in network forensics,
which, provided that the packet details captured are sufficiently
detailed, can play back even the entire network traffic for a particular
point in time. This can be used to find traces of nefarious online
behavior, data breaches, unauthorized website access, malware
infection, and intrusion attempts, and to reconstruct image files,
documents, email attachments, etc. sent over the network. This project
focuses on the very basics of packet analysis by capturing the network
data through Wireshark, filtering out the packets which belong to
application layer protocols and displaying statistics related to them
such as the packet count of each protocol and the average packet
length.
Pandas is a python package used for data analysis. Wireshark is a cross-
platform tool capable of capturing vast amounts of data. Using
Wireshark, we made a csv file to perform analysis. Using pandas, doing
packet analysis is simple and functions for basic operations are inbuilt.
We created two functions, the first one to print the packet count of
application layer protocols in the traffic. The second function to find the
average packet size of each application layer protocol in the traffic and
print it.
