#!/usr/bin/python
# -*- coding: utf-8 -*-
# based on a tool by Emre Ovunc.
#
# magic.scan.py.
# let the internet scan the internet.
# 
# The intended purpose for this code is to scan the internet. 
# It indeed scans the internet, very poorly and slow.
# That is why I like it.
# You see, I do not care about the speed of the scan, or even its results. 
# There are some people that do not like port scans at all, and label them "malicious" and "dangerous".
# They put our IP addresses on black lists and our hosting companies get angry with us...
# But...
# What if *everyone* was port scanning the internet? It's not illegal, and its good to help spread info!
# So that's what we'll do. Magic port scans to make us all equals again :)
# xoxox
# bla
# cko
# ut2
# 019


from scapy.all import *
import os
import sys
import random
import getopt

# remove this idiotic method of warning about requirements, lol.
#print "** You need scapy and a box capable of spoofing IPv4 packets for this magic to work. **"

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def scanpacket(dstPort,counter):
	total = 0
	print "The internet is now scanning itself..."
# print statements work differently with python3 so fml i guess i need to fix all these. 

	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = randomIP()

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow
		TCP_Packet.options = [('MSS', 1460)]

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
        sys.stdout.write("\nWe did it! :3 - Total packets sent: %i\n" % total)


def info():
	os.system("clear")
        print ""
        print "｡･:*:･ﾟ★,｡･:*:･ﾟ☆  :[ PORT SCAN THE PLANET!! ]: ｡･:*:･ﾟ★,｡･:*:･ﾟ☆"
        print ""
        if len(sys.argv) > 1:
            commandline = sys.argv[1]
            print "W0000P - CAUGHT ARG FROM CMDLINE TO SCAN DIS PORT " + sys.argv[1]
            dstPort = sys.argv[1] 
        else:
                commandline = ''
                print "Seems quiet on the command line - usage is magic.py [TCP-PORT] [Seconds]"
                dstPort = input ("CTRL+C out of this and rerun. Will fix interactive later.")
# This actually worked before but i think i fucked it up when i was drunk. will fix interactive later, maybe.

	
	return int(dstPort)
	

def main():
	dstPort = info()
#	counter = input ("Packet Count : ")
        counter = sys.argv[2]
        print sys.argv[2] +" sparkles around the internet :)"
        scanpacket(dstPort,int(counter))

main()
