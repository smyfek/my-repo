#! /usr/bin/env python
import csv
import base64
import subprocess
import itertools
from itertools import islice
import os

# Clear the screen
subprocess.call('clear', shell=True)


bad_words = ['Enter', 'configuration', 'commands,', 'one', 'per', 'line.', 'End', 'with', 'CNTL/Z.', 'config term', 'do sh int status | i XWEB']

with open('result.txt', 'r') as badfile, open('Clean_output.txt', 'w') as cleanfile:
    for line in badfile:
        clean = True
        for word in bad_words:
            if word in line:
                clean = False
        if clean == True:
            cleanfile.write(line)
# clean up temp file
#os.remove('OVENS_HUA_result.csv')
