#!/usr/bin/python
from Tkinter import Tk, Label, Button
from picamera import PiCamera
from time import sleep
from datetime import datetime
import subprocess
camera = PiCamera()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("AlphaPi")

        self.label = Label(master, text="Alpha Particle detector")
        self.label.pack()

        self.greet_button = Button(master, text="Video", command=self.greet)
        self.greet_button.pack()

        self.picture_button = Button(master, text="Picture", command=self.picture)
        self.picture_button.pack()
        
    def greet(self):
        date_string = datetime.now().strftime("%Y-%m-%d-%H:%M")
        camera.start_preview()
        camera.annotate_text = "Alpha Particles!!!"
        camera.brightness = 30
        camera.start_recording('/home/pi/Desktop/alphaVideo-' + date_string + '.h264')
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()
        filename=('alphaVideo' +date_string + 'h264')

    def picture(self):
        date_string = datetime.now().strftime("%Y-%m-%d-%H:%M")
        camera.start_preview()
        camera.annotate_text = "Alpha Particles!!!"
        camera.brightness = 30 
        sleep(10)
        camera.capture('/home/pi/Desktop/alphaimage-' + date_string + '.jpg')
        camera.stop_preview()

root = Tk()
root.geometry("200x100")
my_gui = MyFirstGUI(root)
root.mainloop()
