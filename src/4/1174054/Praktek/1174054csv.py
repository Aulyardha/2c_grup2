# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:33:12 2019

@author: Aulyardha Anindita
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('teori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('teori.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174023', 'nama': 'Aulya', 'kelas': 'D4TI2C', 'tanggal lahir': '23/09/1999'})
        writer.writerow({'npm': '1174009', 'nama': 'Dita', 'kelas': 'D4TI2C', 'tanggal lahir': '23/09/1999'})
