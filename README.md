# MagicPacketGenerator
This script's main intent is to be a performance art piece to draw attention to a dangerous trend of labeling any IP address scanning the internet as "malicious" and "dangerous". Port scans are not illegal. Port scans are not dangerous. Port scans can also be faked. 

This script creates a little magic on the internet by pretending to portscan from random networks. 

Example tcpdump output:

IP 114.237.39.36.6763 > 28.80.64.239.31337: Flags [S], seq 2142, win 2415, options [mss 1460], length 0
IP 32.37.53.68.8809 > 214.74.209.232.31337: Flags [S], seq 1537, win 4924, options [mss 1460], length 0
IP 210.170.117.197.2401 > 6.197.170.137.31337: Flags [S], seq 5290, win 8684, options [mss 1460], length 0
IP 111.122.227.206.6792 > 46.21.91.167.31337: Flags [S], seq 8188, win 3883, options [mss 1460], length 0
IP 254.231.250.31.5258 > 138.183.16.118.31337: Flags [S], seq 2052, win 7842, options [mss 1460], length 0
IP 174.210.126.68.2414 > 46.31.37.108.31337: Flags [S], seq 2777, win 6431, options [mss 1460], length 0
IP 45.201.238.57.6771 > 7.75.23.249.31337: Flags [S], seq 5468, win 2544, options [mss 1460], length 0
IP 219.148.107.1.7757 > 209.175.9.79.31337: Flags [S], seq 1211, win 5187, options [mss 1460], length 0
IP 49.174.78.125.8862 > 123.191.217.45.31337: Flags [S], seq 1668, win 6276, options [mss 1460], length 0
IP 8.225.111.250.4674 > 107.181.135.243.31337: Flags [S], seq 1909, win 2892, options [mss 1460], length 0
IP 51.241.228.117.8605 > 140.198.163.109.31337: Flags [S], seq 7504, win 2333, options [mss 1460], length 0
IP 163.9.169.187.6930 > 176.1.5.220.31337: Flags [S], seq 6994, win 2458, options [mss 1460], length 0
IP 56.64.55.59.7407 > 169.198.154.15.31337: Flags [S], seq 7859, win 4156, options [mss 1460], length 0
IP 18.206.203.255.7243 > 255.88.93.216.31337: Flags [S], seq 3530, win 2403, options [mss 1460], length 0
IP 162.243.57.39.5824 > 118.122.235.217.31337: Flags [S], seq 5674, win 1890, options [mss 1460], length 0
IP 191.195.146.34.8997 > 209.115.32.221.31337: Flags [S], seq 1945, win 5822, options [mss 1460], length 0
IP 126.247.104.26.5004 > 34.94.185.249.31337: Flags [S], seq 2150, win 2683, options [mss 1460], length 0
IP 72.57.72.204.4443 > 123.102.55.216.31337: Flags [S], seq 4548, win 1925, options [mss 1460], length 0
IP 64.103.25.228.6477 > 188.205.104.44.31337: Flags [S], seq 6630, win 8923, options [mss 1460], length 0
IP 216.46.143.157.1971 > 109.39.106.11.31337: Flags [S], seq 1842, win 3942, options [mss 1460], length 0

REQUIREMENTS FOR THIS TO WORK PROPERLY:

Python3

Scapy Python3 libraries (python-scapy)

IPHM-Enabled Server(s) AKA Spoof Boxes AKA Servers without BCP38 turned on.

Sense of Humor


Having a server that's able to spoof IPv4 addresses is certainly the most important part of this performance piece. You can't participate in this without one, sorry. This is also known as IPHM or IP Header Modification enabled servers. They're not easy to find, but there are plenty of them. Contact me if you need assistance with this. twitter.com/notdan


