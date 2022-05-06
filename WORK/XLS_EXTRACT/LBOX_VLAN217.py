#! /usr/bin/env python
from datetime import date
dt = str(date.today())

import os
import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.45.xlsx').sheet_by_index(0)
plik = open("LBOX_VLAN217.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 2).value)+","+
        str(sh.cell(rownum, 69).value)+","+
        str(sh.cell(rownum, 109).value)+ "\n")

finally:
    plik.close()
# replacing cell D1 with "Gateway" value	
import csv
r = csv.reader(open('LBOX_VLAN217.csv')) # Here your csv file
lines = list(r)
lines[0][1] = 'Gateway'
lines[0][2] = 'Mask'
writer = csv.writer(open('LBOX_newIP_'+dt+'.csv', 'w'))
writer.writerows(lines)
