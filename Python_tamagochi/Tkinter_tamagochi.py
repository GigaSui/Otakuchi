from tkinter import *

class Config_root:
    def size():
        root.geometry("240x320")
    def background():
        root.config(bg='white')
    def title():
        root.title("Otakuchi")

class Windows:
    def choice_naruto():
        root.destroy() # Close the root window

        choice_naruto_w = Tk()

        # Config
        choice_naruto_w.geometry("240x320")
        choice_naruto_w.config(bg='white')
        choice_naruto_w.title("Otakuchi")

        # Choices
        Label(choice_naruto_w, text="Please choose your character : ", fg='black', bg='white').pack()
        choices = Frame(choice_naruto_w).pack()
        naruto_number = Label(choices, text="1. ", fg='black', bg='white').pack()
        naruto_btn = Button(choices, text="Naruto").pack()
        hinata_number = Label(choices, text="2. ", fg='black', bg='white').pack()
        hinata_btn = Button(choices, text="Hinata").pack()
        sasuke_number = Label(choices, text="3. ", fg='black', bg='white').pack()
        sasuke_btn = Button(choices, text="Sasuke").pack()

        choice_naruto_w.mainloop()

    def choice_demon_slayer():
        root.destroy() # Close the root window

        choice_demon_slayer_w = Tk()

        # Config
        choice_demon_slayer_w.geometry("240x320")
        choice_demon_slayer_w.config(bg='white')
        choice_demon_slayer_w.title("Otakuchi")

        # Choices
        Label(choice_demon_slayer_w, text="Please choose your character : ", fg='black', bg='white').pack()
        choices = Frame(choice_demon_slayer_w).pack()
        naruto_number = Label(choices, text="1. ", fg='black', bg='white').pack()
        naruto_btn = Button(choices, text="Tanjiro").pack()
        hinata_number = Label(choices, text="2. ", fg='black', bg='white').pack()
        hinata_btn = Button(choices, text="Zenitsu").pack()
        sasuke_number = Label(choices, text="3. ", fg='black', bg='white').pack()
        sasuke_btn = Button(choices, text="Nezuko").pack()

    def choice_one_puch_man():
        root.destroy() # Close the root window

        choice_one_punch_man_w = Tk()

        # Config
        choice_one_punch_man_w.geometry("240x320")
        choice_one_punch_man_w.config(bg='white')
        choice_one_punch_man_w.title("Otakuchi")

        # Choices
        Label(choice_one_punch_man_w, text="Please choose your character : ", fg='black', bg='white').pack()
        choices = Frame(choice_one_punch_man_w).pack()
        naruto_number = Label(choices, text="1. ", fg='black', bg='white').pack()
        naruto_btn = Button(choices, text="Saitama").pack()
        hinata_number = Label(choices, text="2. ", fg='black', bg='white').pack()
        hinata_btn = Button(choices, text="Genos").pack()
        sasuke_number = Label(choices, text="3. ", fg='black', bg='white').pack()
        sasuke_btn = Button(choices, text="Sonic").pack()

class Menu:
    def choice_a():
        Label(root, text="Please choose your anime : ", fg='black', bg='white').pack()
        choices = Frame(root).pack()
        naruto_number = Label(choices, text="1. ", fg='black', bg='white').pack()
        naruto_btn = Button(choices, text="Naruto", command=Windows.choice_naruto).pack()
        demon_slayer_number = Label(choices, text="2. ", fg='black', bg='white').pack()
        demon_slayer_btn = Button(choices, text="Demon Slayer", command=Windows.choice_demon_slayer).pack()
        one_punch_man_number = Label(choices, text="3. ", fg='black', bg='white').pack()
        one_punch_man_btn = Button(choices, text="One Punch Man", command=Windows.choice_one_puch_man).pack()


root = Tk()

# Config of window from a class
Config_root.size()
Config_root.background()
Config_root.title()

Menu.choice_a()

root.mainloop()