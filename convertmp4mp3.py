
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
import os as qq

def jalan(*args):
    root = Tk()
    root.title("Konversi MP4 ke MP3 || Livio Hardi Project")
    root.geometry("400x200")

    def browse_file():
        global filename
        filename = filedialog.askopenfilename()

    def convert_file():
        video = VideoFileClip(filename)
        audio = video.audio
        audio.write_audiofile(filename[:-4] + ".mp3")
        audio.close()
        video.close()
        hasil_label.config(text="Konversi selesai")

    browse_button = Button(root, text="Pilih file MP4", command=browse_file)
    browse_button.pack()

    convert_button = Button(root, text="Konversi ke MP3", command=convert_file)
    convert_button.pack()

    hasil_label = Label(root, text="")
    hasil_label.pack()

    root.mainloop()
    qq.system("clear")

