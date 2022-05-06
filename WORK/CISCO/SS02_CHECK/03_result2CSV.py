#! /usr/bin/env python
import csv
import base64
import subprocess
import itertools
from itertools import islice
import os

# Clear the screen
subprocess.call('clear', shell=True)



#with open('result.txt', 'r') as text_f:
    #print(output, file=text_f)

try:
    from itertools import zip_longest as zip
except ImportError: # will be 3.x series
    pass
# converting raw output txt to CSV file
with open('result.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace(","," ").split() for line in lines]
    grouped = zip(*[stripped]*1)
    with open('SS02_result.csv', 'w') as out_file:
        writer = csv.writer(out_file)
    #writer.writerow(('PORT', 'DEVICE','STATUS'))
        for group in grouped:
            writer.writerows(group)

# slicing first 8 rows from the output file
#with open('OVENS_HUA_result.csv', 'r') as f_input, open('READY.csv', 'w') as f_output:
#    csv_input = csv.reader(f_input)
#    csv_output = csv.writer(f_output)
#    csv_output.writerow(next(csv_input))
#    csv_output.writerows(islice(csv_input, 1, 11, None))

# clean up temp file
#os.remove('OVENS_HUA_result.csv')
