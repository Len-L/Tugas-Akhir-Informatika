
from tkinter import *
import math
import os as qq

def jalan(*args):
    root = Tk()
    root.title("Kalkulator Fisika || Livio Hardi Project")
    root.geometry("400x400")

    def hitung_percepatan():
        try:
            jarak = float(jarak_entry.get())
            waktu = float(waktu_entry.get())
            percepatan = jarak / (waktu ** 2)
            hasil_label.config(text="Percepatan: " + str(percepatan) + " m/s^2")
        except ValueError:
            hasil_label.config(text="Masukkan angka yang valid")

    def hitung_gaya():
        try:
            massa = float(massa_entry.get())
            percepatan = float(percepatan_entry.get())
            gaya = massa * percepatan
            hasil_label.config(text="Gaya: " + str(gaya) + " N")
        except ValueError:
            hasil_label.config(text="Masukkan angka yang valid")

    def hitung_energi_kinetik():
        try:
            massa = float(massa_entry.get())
            kecepatan = float(kecepatan_entry.get())
            energi_kinetik = 0.5 * massa * (kecepatan ** 2)
            hasil_label.config(text="Energi Kinetik: " + str(energi_kinetik) + " J")
        except ValueError:
            hasil_label.config(text="Masukkan angka yang valid")

    jarak_label = Label(root, text="Jarak (m):")
    jarak_label.pack()

    jarak_entry = Entry(root)
    jarak_entry.pack()

    waktu_label = Label(root, text="Waktu (s):")
    waktu_label.pack()

    waktu_entry = Entry(root)
    waktu_entry.pack()

    percepatan_button = Button(root, text="Hitung Percepatan", command=hitung_percepatan)
    percepatan_button.pack()

    massa_label = Label(root, text="Massa (kg):")
    massa_label.pack()

    massa_entry = Entry(root)
    massa_entry.pack()

    percepatan_label = Label(root, text="Percepatan (m/s^2):")
    percepatan_label.pack()

    percepatan_entry = Entry(root)
    percepatan_entry.pack()

    gaya_button = Button(root, text="Hitung Gaya", command=hitung_gaya)
    gaya_button.pack()

    massa_label = Label(root, text="Massa (kg):")
    massa_label.pack()

    massa_entry = Entry(root)
    massa_entry.pack()

    kecepatan_label = Label(root, text="Kecepatan (m/s):")
    kecepatan_label.pack()

    kecepatan_entry = Entry(root)
    kecepatan_entry.pack()

    energi_kinetik_button = Button(root, text="Hitung Energi Kinetik", command=hitung_energi_kinetik)
    energi_kinetik_button.pack()

    hasil_label = Label(root, text="")
    hasil_label.pack()

    root.mainloop()
    qq.system("clear")
