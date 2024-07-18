from tkinter import *
import random
import time

class Reactions:

    def __init__(self):

        self.reactions = Tk()

        def valid():
            self.reactions.destroy()

            Reactions()

        # Config
        self.reactions.geometry("240x320")
        self.reactions.title("Otakushi")
        self.reactions.maxsize(240, 320)
        self.reactions.minsize(240, 320)
        self.reactions.config(bg='white')

        self.reacts = random.randint(1, 4)

        if self.reacts == 1:
            self.k1 = Label(self.reactions, text="Is hungry", bg='white', font=('Arrial', 10, 'bold')).pack()
            self.wtd = Entry(self.reactions).pack(fill=X)
            self.wtd_button = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X)

        if self.reacts == 2:
           self.k2 = Label(self.reactions, text="Is dirty", bg='white', font=('Arrial', 10, 'bold')).pack()
           self.wtd2 = Entry(self.reactions).pack(fill=X)
           self.wtd2_button = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X)
                
        if self.reacts == 3:
            self.k3 = Label(self.reactions, text="Is sick", bg='white', font=('Arrial', 10, 'bold')).pack()
            self.wtd3 = Entry(self.reactions).pack(fill=X)
            self.wtd3_button = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X)

        if self.reacts == 4:
            self.k4 = Label(self.reactions, text="Wants to play", bg='white', font=('Arrial', 10, 'bold')).pack()
            self.wtd4 = Entry(self.reactions).pack(fill=X)
            self.wtd4_button = Button(self.reactions, text="Validate", command=valid, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack(fill=X)

        self.reactions.mainloop()