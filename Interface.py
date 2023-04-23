from tkinter import *

root = Tk()

root.title("Road Sign Detection and Recognition")

root.geometry('450x150')
lbl = Label(root,text="").pack()
btn = Button(root,text="Video Capture",font=('Ariel',12)).pack()
lbl = Label(root,text="").pack()
btn = Button(root,text="Check by uploading an Image",font=('Ariel',12)).pack()

root.mainloop()
