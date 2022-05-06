#print ('') # Print heading
print ('Devices with bad software versions')
print ('==================================')

# Set Variable for current version comparison used in Step 4

current_version = ('3.9.1_BT')

# Read all lines of device information from file
import xlrd

sh = xlrd.open_workbook('Upgrade Schedule.xlsx').sheet_by_index(0)
file = open("output_ver.txt", 'w')


try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 1).value)+","+
        str(sh.cell(rownum, 2).value)+","+
        str(sh.cell(rownum, 3).value)+ "\n")

#device_info_list = line.strip().split(',') # Get device info into list

# Put device information into dictionary for this one device
#device_info = {} # Create the inner dictionary of device info
#device_info['store'] = device_info_list[0]
#device_info['ip'] = device_info_list[2]
#device_info['version'] = device_info_list[3]

# If the version doesn't match our 'current version', print out warning
#if device_info['version'] != current_version:
#    print '      Device:', device_info['store'], '   Version:', device_info['version']

finally:
device_info_list = line.strip().split(',') # Get device info into list
# Put device information into dictionary for this one device
device_info = {} # Create the inner dictionary of device info
device_info['store'] = device_info_list[0]
device_info['ip'] = device_info_list[2]
device_info['version'] = device_info_list[3]

# If the version doesn't match our 'current version', print out warning
if device_info['version'] != current_version:
    print ('      Device:', device_info['store'], '   Version:', device_info['version'])

file.close() # Close the file since we are done with it
