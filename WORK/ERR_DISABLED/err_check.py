#! /usr/bin/env python
#import base64
#u = base64.b64decode(b'YXJ0dXJr')
#p = base64.b64decode(b'TGlkbDIwMTUu')

#store = input ("Please enter the store number: ")

#switch = input ("Please choose network switch to check (eg.SS01 or SS02): ")

#address = ('gb-'+(store)+'ss01.network.gb.lidl.net')

#print ("connecting to ",address,"...")


#from netmiko import ConnectHandler
#router = {
#'device_type': 'cisco_ios',
#'ip':(address),
#'username': base64.b64decode(b'YXJ0dXJr'),
#'password': base64.b64decode(b'TGlkbDIwMTUu'),
#'port' : 22, # optional, defaults to 22
#'secret': 'pas', # optional, defaults to ''
#'verbose': True, # optional, defaults to True
#}
#net_connect = ConnectHandler(**router)

#output = net_connect.send_command('sh ver | i WS')
#output = config_commands = [
#           'int range Fa0/2-3 , Fa0/17-18 , Fa0/23-24',
#			'switchport access vlan 10',
#           'end']

#output = net_connect.send_config_set('configure terminal')
#output = net_connect.send_config_set(config_commands)
#output = net_connect.save_config()

#print(output,'\n')
#print(output2,'\n')
#print("------------------------- END ---------------------------")
#net_connect.disconnect() # Disconnecting session





from netmiko import ConnectHandler
import getpass
import sys
import time

device = {
    'device_type': 'cisco_ios',
    'ip': '',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }
ipfile=open("iplist.txt")
print ("Script for SSH to device, Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()
device['secret']=getpass.getpass()



for line in ipfile:

 device['ip']=line.strip("\n")
 print("\n\nConnecting Device ",line)
 net_connect = ConnectHandler(**device)
 net_connect.enable()
 time.sleep(2)
 print ("Checking in progres... ")
 
 output = net_connect.send_command('sh ip int brie | i Tun')
 
 #print(output,'\n')
 print("\nOutput from "+line+output,  file=open("tun_result.txt", 'a'))

ipfile.close()



#my_output_file = open('result.txt', 'a')
#my_output_file.write(output)
#print(output), file=my_output_file)
#my_output_file.close()
