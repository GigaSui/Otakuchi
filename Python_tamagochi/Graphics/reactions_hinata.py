from tkinter import *
import random
import time
from PIL import Image, ImageTk

class ReactionsHinata:

    def __init__(self):

        self.reactions = Toplevel()

        def valid():
            self.reactions.destroy()

            ReactionsHinata()

        # Config
        self.reactions.geometry("240x320")
        self.reactions.title("Otakushi")
        self.reactions.maxsize(240, 320)
        self.reactions.minsize(240, 320)
        self.reactions.config(bg='white')

        # Widgets
        self.reacts = random.randint(1, 4)

        if self.reacts == 1:
            self.wtd = Entry(self.reactions).pack(fill=X)
     
            # Load a image
            self.img_path = "assets/Hinata_hungry.png"
            self.image = Image.open(self.img_path)
            self.img = ImageTk.PhotoImage(self.image)

            # Assign the image to a canva
            self.texture = Label(self.reactions, image=self.img, bg='white')
            self.texture.pack()

            # Add the "Vallid" button
            self.wtd_button = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X, side=BOTTOM)

        if self.reacts == 2:
           self.wtd2 = Entry(self.reactions).pack(fill=X)

           # Load a image
           self.img_path2 = "assets/Hinata_dirty.png"
           self.image2 = Image.open(self.img_path2)
           self.img2 = ImageTk.PhotoImage(self.image2)

           # Assign the image to a canva
           self.texture2 = Label(self.reactions, image=self.img2, bg='white')
           self.texture2.pack()

           # Add the "Vallid" button
           self.wtd_button2 = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X, side=BOTTOM)

           time.sleep(random.randint(1, 10))     

        if self.reacts == 3:
            self.wtd3 = Entry(self.reactions).pack(fill=X)

            # Load a image
            self.img_path3 = "assets/Hinata_sick.png"
            self.image3 = Image.open(self.img_path3)
            self.img3 = ImageTk.PhotoImage(self.image3)

            # Assign the image to a canva
            self.texture3 = Label(self.reactions, image=self.img3, bg='white')
            self.texture3.pack()

            # Add the "Vallid" button
            self.wtd_button3 = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X, side=BOTTOM)

            time.sleep(random.randint(1, 10))

        if self.reacts == 4:
            self.wtd4 = Entry(self.reactions).pack(fill=X)

            # Load a image
            self.img_path4 = "assets/Hinata_play.png"
            self.image4 = Image.open(self.img_path4)
            self.img4 = ImageTk.PhotoImage(self.image4)

            # Assign the image to a canva
            self.texture4 = Label(self.reactions, image=self.img4, bg='white')
            #self.texture.create_image()
            self.texture4.pack()

            # Add the "Vallid" button
            self.wtd_button4 = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X, side=BOTTOM)

            time.sleep(random.randint(1, 10))

        self.reactions.mainloop()