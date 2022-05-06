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
from datetime import date
dt = str(date.today())

import os

import xlrd

sh = xlrd.open_workbook('MPLS Service IP Allocation V3.45.xlsx').sheet_by_index(0)
plik = open('BMS IP Allocation_'+dt+'.csv', 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 0).value)+","+
        str(sh.cell(rownum, 2).value)+","+
        str(sh.cell(rownum, 3).value)+","+
        str(sh.cell(rownum, 4).value)+","+
        str(sh.cell(rownum, 8).value)+","+
        str(sh.cell(rownum, 9).value)+ "\n")

finally:
    plik.close()
