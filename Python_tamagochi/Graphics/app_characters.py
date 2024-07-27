from tkinter import *
from playsound import playsound

# Naruto
from reactions_naruto import ReactionsNaruto
from reactions_sasuke import ReactionsSasuke
from reactions_hinata import ReactionsHinata

# Demon Slayer 
from reactions_tanjiro import ReactionsTanjiro

class Naruto:
    def __init__(self):

        self.naruto = Tk()

        playsound('assets/Button_sound.mp3')

        # Config
        self.naruto.geometry("240x320")
        self.naruto.title("Otakushi")
        self.naruto.maxsize(240, 320)
        self.naruto.minsize(240, 320)
        self.naruto.config(bg='white')

        self.title = Label(self.naruto, text="Please choose your character", bg='white', font=('Arrial', 10, 'bold')).pack()

        self.n_label = Label(self.naruto, text="1.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.n = Button(self.naruto, text="Naruto", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold'), command=ReactionsNaruto).pack()
        self.h_label = Label(self.naruto, text="2.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.h = Button(self.naruto, text="Hinata", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold'), command=ReactionsHinata).pack()
        self.s_label = Label(self.naruto, text="3.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.s = Button(self.naruto, text="Sasuke", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold'), command=ReactionsSasuke).pack()
        
        self.naruto.mainloop()

class Demon_slayer:
    def __init__(self):
        self.ds = Tk()

        # Config
        self.ds.geometry("240x320")
        self.ds.title("Otakushi")
        self.ds.maxsize(240, 320)
        self.ds.minsize(240, 320)
        self.ds.config(bg='white')

        self.title = Label(self.ds, text="Please choose your character", bg='white', font=('Arrial', 10, 'bold')).pack()

        self.t_label = Label(self.ds, text="1.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.t = Button(self.ds, text="Tanjiro", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold'), command=ReactionsTanjiro).pack()
        self.z_label = Label(self.ds, text="2.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.z = Button(self.ds, text="Zenitsu", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()
        self.ne_label = Label(self.ds, text="3.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.ne = Button(self.ds, text="Nezuko", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()

        self.ds.mainloop()

class One_punch_man:
    def __init__(self):
        self.opm = Tk()

        # Config
        self.opm.geometry("240x320")
        self.opm.title("Otakushi")
        self.opm.maxsize(240, 320)
        self.opm.minsize(240, 320)
        self.opm.config(bg='white')

        self.title = Label(self.opm, text="Please choose your character", bg='white', font=('Arrial', 10, 'bold')).pack()

        self.s_label = Label(self.opm, text="1.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.s = Button(self.opm, text="Saitama", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()
        self.g_label = Label(self.opm, text="2.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.g = Button(self.opm, text="Genos", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()
        self.so_label = Label(self.opm, text="3.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.so = Button(self.opm, text="Sonic", bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()

        self.opm.mainloop()