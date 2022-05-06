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


import xlrd

sh = xlrd.open_workbook('MPLS IP STORE ALLOCATION V_16.42.xlsx').sheet_by_index(0)
plik = open("NS01_IPs_extract.csv", 'w')

try:
    for rownum in range(sh.nrows):
        plik.write(str(sh.cell(rownum, 2).value)+","+
        #str(sh.cell(rownum, 5).value)+","+
        str(sh.cell(rownum, 32).value)+ "\n")

finally:
    plik.close()
