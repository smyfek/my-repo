#! /usr/bin/env python
# Operacje na plikach:

# Otwarcie plku w trybie odczytu
#plik = open('plik.txt','r')
#plik.close()

# Otwarcie pliku w trybie zapisu
#plik = open('plik.txt','w')
#plik.close()

#Tryb append - tylko dodaje dane na koncu pliku nie kasujac obecnej zawartosci pliku
#plik = open('plik.txt','a')
#plik.close()

#Zapis do pliku
#plik.write(str(55552522))
#plik.write("\n")
#plik.write("Tutaj masz jakis napis")

#import datetime
#dt = str(datetime.datetime.now())

#import datetime
from datetime import date
dt = str(date.today())

import os
import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.37.xlsx').sheet_by_index(0)
plik = open("nagios.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 1).value)+","+
        str(sh.cell(rownum, 3).value)+","+
        str(sh.cell(rownum, 6).value)+","+
        str(sh.cell(rownum, 12).value)+ "\n")

finally:
    plik.close()
# replacing cell D1 with "Gateway" value
import csv
r = csv.reader(open('nagios.csv')) # Here your csv file
lines = list(r)
#lines[0][3] = 'Post Code'
writer = csv.writer(open('Store_Nagios_data_extract_'+dt+'.csv', 'w'))
#writer = csv.writer(open('Store Safelock IP Allocation.csv', 'w'))
writer.writerows(lines)


# importing pandas module
#import pandas as pd

# making data frame from csv file
#data = pd.read_csv("Store_stri.csv", index_col ="Store" )

# dropping passed values
#data.drop(["0"], inplace = True)

# display
#print (data.drop("0"))#, file=open("dropped.csv", 'a'))


#input = open('Store Safelock IP Allocation_'+dt+'.csv', 'r')
#output = open('Safelock_stri2.csv', 'w')
#writer = csv.writer(output)
#for row in csv.reader(input):
#    if row[2]!="0":
#        writer.writerow(row)
#input.close()
#output.close()
#with open('Store Safelock IP Allocation_'+dt+'.csv', 'rb') as inp, open('Safelock_stripped.csv', 'wb') as out:
    #writer = csv.writer(out)

    #    if row[0] != " 0":
        #    writer.writerow(row)
