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
device = {
    'device_type': 'cisco_ios',
    'ip': '',
    'username': 'username',
    'password': 'password',
    'secret':'password'
    }

# For predefined credenatils
#device = {
#    'device_type': 'cisco_ios',
#    'ip': '',
#    'username': base64.b64decode(b'YXJ0dXJr'),
#    'password': base64.b64decode(b'TGlkbDIwMTUu'),
#    'secret': 'password',
#    'default_enter': '\r\n',
    #'session_log': 'my_ssh_error_output.txt',
#    }


# File with ip addresses to connect
ipfile=open("iplist.txt")
# Uncomment for manual credentials input
print ("Script for SSH to device, Please enter your credential")
device['username']=input("User name ")
device['password']=getpass.getpass()
device['secret']=getpass.getpass()
time.sleep(2)
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
        print("Failed connect to "+line,  file=open("failed_rerun.txt", 'a'))
ipfile.close()
net_connect.disconnect()
