import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from SignDetection import *
from Recognition import *

def show_image():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('ALL Files','*.*')]
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=f_types)
    path = Image.open(filename)
    
    img_resized=path.resize((400,400)) # new width & height
    path=ImageTk.PhotoImage(img_resized)
    img = cv2.imread(filename,1)
    cv2.imwrite("Selected Image/image.png",img)
    lbl.configure(image=path)
    lbl.image = path

def detect_upimg():
    lbl.configure(image="")
    filename = "Selected Image/image.png"
    cropped = detect_img(filename)
    
    path = Image.open('Detected Image/Image.png')
    img_resized=path.resize((400,400)) # new width & height
    path=ImageTk.PhotoImage(img_resized)
    cv2.imwrite("Cropped Image/cropped.png",cropped)
    
    lbl.configure(image=path)
    lbl.image = path

def recog_img():
    im = cv2.imread(r'Cropped Image/cropped.png',1)
    recognize_sign(im)
    
root = tk.Tk()

root.title("Road Sign Detection and Recognition Using an Image")

root.geometry('550x550')

lblempty1_0= tk.Label(root,text="")
lblempty1_1= tk.Label(root,text="First you have to Upload the image and the you can detect the road sign.",font=('Ariel',10))
lblempty1_2= tk.Label(root,text="Finally you can recognize the sign!",font=('Ariel',10))

lblempty1= tk.Label(root,text="")
btn_U_I = tk.Button(root,text="Upload an Image",command=lambda:show_image(),font=('Ariel',12))


lblempty2 = tk.Label(root,text="")
lbl=tk.Label(root)

btn_D = tk.Button(root,text="Detect the Road Sign",command=lambda:detect_upimg(),font=('Ariel',12))
lblempty3 = tk.Label(root,text="")

btn_R = tk.Button(root,text="Recognize the Road Sign",command=lambda:recog_img(),font=('Ariel',12))
lblempty4 = tk.Label(root,text="")

lblempty1_0.pack()
lblempty1_1.pack()
lblempty1_2.pack()
lblempty1.pack()
btn_U_I.pack()
lblempty2.pack()
btn_D.pack()
lblempty3.pack()
btn_R.pack()
lblempty4.pack()

lbl.pack()
root.mainloop()

