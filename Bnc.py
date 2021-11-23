#usr/bin/python3
#Contact Me, Darul Febri at WhatsApp :0819-9720-0360

import time
import os
from tqdm import tqdm

skor = 0
WAKTU0= time.clock()
WAKTU1= time.clock()
hasil= WAKTU1 - WAKTU0
os.system("clear")
print("  BNC TESTER")
print(" ")
#a little style doesn't make people mad, does it?
print("MENGUJI PERANGKAT....")
for i in tqdm(range(1000)):
	time.sleep(0.01)
print("WAKTU YANG DITEMPUH : ",hasil)
print(" ")
#UNTUK DATA DIBAWAH BOLEH DITAMBAH ( BIAR HASILNYA MAKIN RINCI )
if hasil >= 0.000000000000000009:
	gg = skor + 5
if hasil >= 0.000000000000000099:
	gg = skor + 10
if hasil >= 0.000000000000009999:
	gg = skor + 15
if hasil >= 0.000000000000999999:
	gg = skor + 20
if hasil >= 0.000000000099999999:
	gg = skor + 25
if hasil >= 0.000000009999999999:
	gg = skor + 30
if hasil >= 0.000000999999999999:
	gg = skor + 35
if hasil >= 0.000099999999999999:
	gg = skor + 40
if hasil >= 0.009999999999999999:
	gg = skor + 45
if hasil >= 0.999999999999999999:
	gg = skor + 50
if hasil >= 1.999999999999999999:
	gg = skor + 55
if hasil >= 2.999999999999999999:
	gg = skor = 60
if hasil >= 3.999999999999999999:
	gg = skor + 65
if hasil >= 4.999999999999999999:
	gg = skor + 70
if hasil >= 5.999999999999999999:
	gg = skor + 75
if hasil >= 6.999999999999999999:
	gg = skor + 80
if hasil >= 7.999999999999999999:
	gg = skor + 85
if hasil >= 8.999999999999999999:
	gg = skor + 90
if hasil >= 9.999999999999999999:
	gg = skor + 95
if hasil >= 10.999999999999999999:
	gg = skor + 100

def hasilnya():
	print("   SKOR PERANGKAT KAMU : ",gg)
hasilnya()
