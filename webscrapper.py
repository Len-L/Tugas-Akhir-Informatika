
import requests
import os as qq
import time as tt

def jalan(*args):
    qq.system("rm output.html")
    print("contoh: https://contohdomain.com")
    url = input("URL Target-> ")
    response = requests.get(url)
    with open('output.html', 'w') as f:
        f.write(response.text)
        print(" ")
        print("Hasil Berhasil disave dalam file 'output.html'")
        tt.sleep(1)
        print("apakah anda ingin melihat hasilnya di cli??")
        bertanya = input("ya/tidak? ")
        if bertanya=="ya":
            qq.system("clear ; echo ' ' ; cat output.html")
        if bertanya=="tidak":
            print("wokey")
            qq.system("clear")





