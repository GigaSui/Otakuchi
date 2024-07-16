from tkinter import *

from app_characters import *

class App_animes:
    def __init__(self):
        self.root = Tk()

        # Config
        self.root.geometry("240x320")
        self.root.title("Otakushi")
        self.root.maxsize(240, 320)
        self.root.minsize(240, 320)

        # Widgets
        self.label = Label(self.root, text="Please choose your anime").pack()

        self.center_frame = Frame(self.root).pack()

        self.naruto_label = Label(self.center_frame, text="1.").pack()
        self.naruto_button = Button(self.root, text="Naruto", command=Naruto).pack()

        self.demon_slayer_label = Label(self.center_frame, text="2.").pack()
        self.demon_slayer_button = Button(self.root, text="Demon Slayer", command=Demon_slayer).pack()

        self.one_punch_man_label = Label(self.center_frame, text="3.").pack()
        self.one_punch_man_button = Button(self.root, text="One Punch Man", command=One_punch_man).pack()

        self.root.mainloop()