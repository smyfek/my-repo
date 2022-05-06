#! /usr/bin/env python

import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.42.xlsx').sheet_by_index(0)
plik = open("NS02_IPs_extract.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 2).value)+","+
        #str(sh.cell(rownum, 5).value)+","+
        str(sh.cell(rownum, 33).value)+ "\n")

finally:
    plik.close()
