from netmiko import ConnectHandler
import getpass
import sys
import time
import base64
import paramiko
import netmiko
import subprocess
import csv
import itertools
from itertools import islice
import os

from datetime import datetime

# Converting datetime object to string
dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S")

###################### Execution Time calculation #########################
#import time
#from datetime import timedelta

#start_time = time.time()

#
# Perform lots of computations.
#

#elapsed_time_secs = time.time() - start_time

#msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))

#print(msg)

#############################################################################

# For manual credentials input - use code below
#device = {
    #'device_type': 'cisco_ios',
    #'ip': '',
    #'username': 'username',
    #'password': 'password',
    #'secret':'password'
    #}

# For predefined credenatils

device = {
    'device_type': 'huawei',
    'ip': '',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }
# Clear the screen
subprocess.call('clear', shell=True)


# File with ip addresses to connect
ipfile=open("iplist.txt")
# Uncomment for manual credentials input
print ("Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()
device['secret']=getpass.getpass()
time.sleep(1)
configfile=open("configfile.txt")
configset=configfile.read()
configfile.close()

for line in ipfile:
    try:
        device['ip']=line.strip("\n")
        print("Connecting",line)
        net_connect = ConnectHandler(**device)
        time.sleep(1)
        net_connect.enable()
        time.sleep(1)
        #print ("checking in progres... ")
        output = net_connect.send_config_set(configset)
        #output = net_connect.send_command('display port vlan GigabitEthernet0/0/19')
        #print(output,'\n')
        print(output, file=open("result.txt", 'a'))
        #print ("Device",line, "### checked successfully ###")
        #print(output)
    #except (paramiko.AuthenticationException, netmiko.NetMikoTimeoutException, netmiko.NetMikoAuthenticationException, ValueError, EOFError):
    #    print ("Failed connect to "+line, file=open("failed.txt", 'a'))
    #print ("Failed connect to "+line, timestampStr, file=open("failed.txt", 'a'))
    except (paramiko.AuthenticationException, netmiko.NetMikoAuthenticationException):
        print("Authentication failed, please verify your credentials:"+line)
    except netmiko.NetMikoTimeoutException:
        print("Unable to establish SSH connection(timeout):"+line)
    except Exception as e:
        print(e.args)
        print("Failed connect to "+line,  file=open("failed.txt", 'a'))
ipfile.close()
net_connect.disconnect()


bad_words = ['view,', 'system', 'Enter', 'Ctrl+Z.', 'with', 'view', 'user', 'return', 'system-view']

with open('result.txt', 'r') as badfile, open('Clean_output.txt', 'w') as cleanfile:
    for line in badfile:
        clean = True
        for word in bad_words:
            if word in line:
                clean = False
        if clean == True:
            cleanfile.write(line)
