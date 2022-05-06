#! /usr/bin/env python
import csv
import base64
import subprocess
import itertools
from itertools import islice
import os

# Clear the screen
subprocess.call('clear', shell=True)

store = input ("Please enter the store number: ")
switch = input ("Please select switch to check (1, 2, 3 or 4): ")

address = ('lgb'+(store)+'-nwprsw'+'-p00'+(switch)+'.network.gb.lidl.net')

print ("connecting to ",address,"...")

from netmiko import ConnectHandler
router = {
'device_type': 'huawei',
'ip':(address),
'username': base64.b64decode(b'jakis user'),
'password': base64.b64decode(b'jakies haslo'),
'port' : 22, # optional, defaults to 22
'secret': 'pas', # optional, defaults to ''
'verbose': True, # optional, defaults to True
}

net_connect = ConnectHandler(**router)

output = net_connect.send_command('display interface description | i Printer')

print(output,'\n')
print("------------------------- Data Extracted successfuly ---------------------------")
net_connect.disconnect() # Disconnecting session

with open('rawdata.txt', 'w') as text_f:
    print(output, file=text_f)

try:
    from itertools import zip_longest as zip
except ImportError: # will be 3.x series
    pass
# converting raw output txt to CSV file
with open('rawdata.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace(","," ").split() for line in lines]
    grouped = zip(*[stripped]*1)
    with open((store)+'_HUAWEI_SS0'+(switch)+'.csv', 'w') as out_file:
        writer = csv.writer(out_file)
    #writer.writerow(('PORT', 'DEVICE','STATUS'))
        for group in grouped:
            writer.writerows(group)

# slicing first 8 rows from the output file
with open((store)+'_HUAWEI_SS0'+(switch)+'.csv', 'r') as f_input, open((store)+'-HUAWEI-SS0'+(switch)+'.csv', 'w') as f_output:
    csv_input = csv.reader(f_input)
    csv_output = csv.writer(f_output)
    csv_output.writerow(next(csv_input))
    csv_output.writerows(islice(csv_input, 8, None))

# clean up temp file
os.remove((store)+'_HUAWEI_SS0'+(switch)+'.csv')
