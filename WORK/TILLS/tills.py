#! /usr/bin/env python
import base64
u = base64.b64decode(b'jakis username')
p = base64.b64decode(b'jekies password')

store = input ("Please enter the store number: ")

switch = input ("Please choose network switch to check (eg.NS01 or NS02): ") 

address = ('gb-'+(store)+(switch)+'.network.gb.lidl.net')

print ("connecting to ",address,"...")


from netmiko import ConnectHandler
router = {
'device_type': 'cisco_ios',
'ip':(address),
'username': base64.b64decode(b'jakis user'),
'password': base64.b64decode(b'jakies password'),
'port' : 22, # optional, defaults to 22
'secret': 'pas', # optional, defaults to ''
'verbose': True, # optional, defaults to True
}
net_connect = ConnectHandler(**router)

output1 = net_connect.send_command('show int status | i TILL')
output2 = net_connect.send_command('show mac address-table | i 0001.')

print(output1,'\n')
print(output2,'\n')
print("------------------------- END ---------------------------")
net_connect.disconnect() # Disconnecting session


