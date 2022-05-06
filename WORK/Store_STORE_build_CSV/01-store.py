#! /usr/bin/env python
import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.24.xlsx').sheet_by_index(0)
plik = open("store.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 1).value)+","+
        str(sh.cell(rownum, 3).value)+","+
        str(sh.cell(rownum, 7).value)+","+
        str(sh.cell(rownum, 85).value)+ "\n")

finally:
    plik.close()

import csv
r = csv.reader(open('store.csv')) # Here your csv file
lines = list(r)
lines[0][0] = 'store_id'
lines[0][1] = 'name'
lines[0][2] = 'warehouse_id'
lines[0][3] = 'ipv4'
#writer = csv.writer(open('Store Safelock IP Allocation_'+dt+'.csv', 'w'))
writer = csv.writer(open('store_ready.csv', 'w'))
writer.writerows(lines)
