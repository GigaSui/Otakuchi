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

        self.reacts = random.randint(1, 4)

        if self.reacts == 1:
            self.k1 = Label(self.reactions, text="Is hungry").pack()
            self.wtd = Entry(self.reactions).pack(fill=X)
            self.wtd_button = Button(self.reactions, text="Validate", command=valid).pack(fill=X)

        if self.reacts == 2:
           self.k2 = Label(self.reactions, text="Is dirty").pack()
           self.wtd2 = Entry(self.reactions).pack(fill=X)
           self.wtd2_button = Button(self.reactions, text="Validate", command=valid).pack(fill=X)
                
        if self.reacts == 3:
            self.k3 = Label(self.reactions, text="Is sick").pack()
            self.wtd3 = Entry(self.reactions).pack(fill=X)
            self.wtd3_button = Button(self.reactions, text="Validate", command=valid).pack(fill=X)

        if self.reacts == 4:
            self.k4 = Label(self.reactions, text="Wants to play").pack()
            self.wtd4 = Entry(self.reactions).pack(fill=X)
            self.wtd4_button = Button(self.reactions, text="Validate", command=valid).pack(fill=X)

        self.reactions.mainloop()