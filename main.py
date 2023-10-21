
import kalkulator
import webscrapper
import fisika
import convertmp4mp3
import time as tt 
import qrcodeLi
import os as qq

while True:
    print(" ")
    print(" ")
    qq.system("figlet 'Livio Hardi \n Informatika 2' ")
    print(" ")
    print(" ")
    print("1. Kalkulator GUI")
    print("2. Kalkulator Fisika  ")
    print("3. Convert MP4 Ke MP3 'Vidio Ke Music' ")
    print("4. Web Scrapper")
    print("5. Membuat QR Code")
    print("99. Keluar")
    print("")
    a = input("pilih salah satu-> ")

    if a=="1":
        print("Berhasil jalan dengan baik")
        kalkulator.jalan()

    if a=="4":
        webscrapper.jalan()

    if a=="2":
        fisika.jalan()
    
    if a=="3":
        convertmp4mp3.jalan()

    if a=="5":
        qrcodeLi.jalan()

    if a=="99":
        print(" ")
        print("Created By: \n Livio Hardi 'LeonTech'  \n Informatika 2 \n SMA Negeri 1 Berau")
        tt.sleep(1)
        print(" ")
        break



