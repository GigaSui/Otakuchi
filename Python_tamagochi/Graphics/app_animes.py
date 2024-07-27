from tkinter import *

from app_characters import *

class App_animes:

    def sounds(self):
        pass

    def __init__(self):
        self.root = Tk()

        # Config
        self.root.geometry("240x320")
        self.root.title("Otakushi")
        self.root.maxsize(240, 320)
        self.root.minsize(240, 320)
        self.root.config(bg='white')

        # Widgets
        self.label = Label(self.root, text="Please choose your anime", bg='white', font=('Arrial', 10, 'bold')).pack()

        self.center_frame = Frame(self.root).pack()

        self.naruto_label = Label(self.center_frame, text="1.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.naruto_button = Button(self.root, text="Naruto", command=Naruto, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()

        self.demon_slayer_label = Label(self.center_frame, text="2.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.demon_slayer_button = Button(self.root, text="Demon Slayer", command=Demon_slayer, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()

        self.one_punch_man_label = Label(self.center_frame, text="3.", bg='white', font=('Arrial', 10, 'bold')).pack()
        self.one_punch_man_button = Button(self.root, text="One Punch Man", command=One_punch_man, bg='black', fg='white', activebackground='white', activeforeground='black', font=('Arrial', 10, 'bold')).pack()

        self.root.mainloop()