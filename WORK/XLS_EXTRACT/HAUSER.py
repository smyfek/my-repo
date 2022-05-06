#! /usr/bin/env python
from datetime import date
dt = str(date.today())

import os
import xlrd


sh = xlrd.open_workbook('MPLS Service IP Allocation V3.45.xlsx').sheet_by_index(0)
plik = open("HAUSER.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 0).value)+","+
        str(sh.cell(rownum, 2).value)+","+
        str(sh.cell(rownum, 3).value)+","+
        str(sh.cell(rownum, 4).value)+","+
        str(sh.cell(rownum, 10).value)+ "\n")

finally:
    plik.close()
# replacing cell D1 with "Gateway" value
import csv
r = csv.reader(open('HAUSER.csv')) # Here your csv file
lines = list(r)
#lines[0][2] = 'Gateway'
writer = csv.writer(open('HAUSER_'+dt+'.csv', 'w'))
writer.writerows(lines)