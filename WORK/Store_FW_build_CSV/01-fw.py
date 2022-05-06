#! /usr/bin/env python
import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.24.xlsx').sheet_by_index(0)
plik = open("fw.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 1).value)+","+
        str(sh.cell(rownum, 7).value)+","+
        str(sh.cell(rownum, 130).value)+","+
        str(sh.cell(rownum, 39).value)+","+
        str(sh.cell(rownum, 50).value)+","+
        str(sh.cell(rownum, 56).value)+","+
        str(sh.cell(rownum, 62).value)+","+
        str(sh.cell(rownum, 65).value)+","+
        str(sh.cell(rownum, 68).value)+","+
        str(sh.cell(rownum, 71).value)+","+
        str(sh.cell(rownum, 74).value)+ "\n")

finally:
    plik.close()

import csv
r = csv.reader(open('fw.csv')) # Here your csv file
lines = list(r)
lines[0][0] = 'store_id'
lines[0][1] = 'wh_id'
lines[0][2] = 'store_net'
lines[0][3] = 'VLAN101'
lines[0][4] = 'VLAN102'
lines[0][5] = 'VLAN103'
lines[0][6] = 'VLAN104'
lines[0][7] = 'VLAN105'
lines[0][8] = 'VLAN106'
lines[0][9] = 'VLAN107'
lines[0][10] = 'VLAN108'
#writer = csv.writer(open('Store Safelock IP Allocation_'+dt+'.csv', 'w'))
writer = csv.writer(open('fw_ready.csv', 'w'))
writer.writerows(lines)
