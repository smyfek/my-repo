from netmiko import ConnectHandler
import getpass
import sys
import time
import base64
import paramiko
import netmiko

from datetime import datetime

# Converting datetime object to string
dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S")

###################### Execution Time calculation #########################
import time
from datetime import timedelta

start_time = time.time()

###############
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
#device['secret']='password'
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
        print ("Configuration in progres... ")
        output = net_connect.send_config_set(configset)
        print ("Device",line, "### Completed successfully ###")
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


elapsed_time_secs = time.time() - start_time

msg1 = "------------------------------"
msg2 = "                                              "
msg3 = " Execution took: %s secs  " % timedelta(seconds=round(elapsed_time_secs))
msg4 = "                                              "
msg5 = "------------------------------"

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
