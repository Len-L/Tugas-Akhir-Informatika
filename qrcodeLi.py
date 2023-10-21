
import subprocess as qq

def jalan(*args):
    hasil = input("Masukan URL Atau Text Untuk Di Jadikan QR Code-> ")
    qq.run(["qr", hasil])
    tanya = input("ketik 'ya' jika selesai-> ")
    if tanya=="ya":
        qq.run(["clear"])


