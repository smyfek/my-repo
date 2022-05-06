#!/usr/bin/env python
import os

reached = []                           					# Empty lists to collect reachable hosts
not_reached = []                         				# Empty list to collect unreachable hosts

with open('ip-source.txt') as file:						# Collecting ip addresses from the file
    dump = file.read()
line = dump.splitlines()
	
for ip in line:
	ping_test = os.popen(f"ping -c1 {ip}").read()
	if "1 packets received" in ping_test:              	# If received 1 packet then it's reachable
		reached.append(ip)
		print(f"Host ** {ip} ** is UP ")
	else: 												# Otherwise is down
		not_reached.append(ip)
		print(f"Host ** {ip} ** is DOWN") 				
print()													# Printing results ###
print('*'*5+' Ping response = UP '+'*'*5)
print(*reached, sep = "\n") 
print()
print('*'*5+' Ping response = DOWN '+'*'*5)
print(*not_reached, sep = "\n") 
print()													# Saving output to the files
print(*not_reached, sep = "\n", file=open("HostsDOWN.txt","w"))
print(*reached, sep = "\n", file=open("HostsUP.txt","w"))
file.close()
