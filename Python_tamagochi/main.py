import random
import time

def main():
    print("""
    ________   __          __                  __     __ 
    \_____  \_/  |______  |  | ____ __   ____ |  |__ |__|
     /   |   \   __\__  \ |  |/ /  |  \_/ ___\|  |  \|  |
    /    |    \  |  / __ \|    <|  |  /\  \___|   Y  \  |
    \_______  /__| (____  /__|_ \____/  \___  >___|  /__|
            \/          \/     \/           \/     \/    
    """)

def choice_a():
    # Anime's list 
    print("1. Naruto")
    print("2. Demon Slayer")
    print("3. One Punch Man")

class Menu():
    def naruto():
        print("1. Naruto")
        print("2. Hinata")
        print("3. Sasuke")
        n = int(input("Please choice your character : "))
    def demon_slayer():
        print("1. Tanjiro")
        print("2. Zenitsu")
        print("3. Nezuko")
        ds = int(input("Please choice your character : "))
    def one_punch_man():
        print("1. Saitama")
        print("2. Genos")
        print("3. Sonic")
        opm = int(input("Please choice your character : "))

def choice_c():
    choice_a = int(input("Please select your anime : "))
    if choice_a == 1:
        Menu.naruto()
    if choice_a == 2:
        Menu.demon_slayer()
    if choice_a == 3:
        Menu.one_punch_man()

def reactions():
    while True:
        react = random.randint(1, 4)

        global k1
        global k2
        global k3
        global k4

        if react == 1:
            k1 = str
            while k1 != "eat":
                print("Is hungry")
                k1 = input("What to do ? ")
                print("Is no longer hungry !")
            time.sleep(random.randint(1, 10))
        if react == 2:
            k2 = str
            while k2 != "clean":
                print("Is dirty")
                k2 = input("What to do ? ")
                print("Is clean !")
            time.sleep(random.randint(1, 10))
        if react == 3:
            k3 = str
            while k3 != "heals":
                print("Is sick")
                k3 = input("What to do ? ")
                print("Is heals !")
            time.sleep(random.randint(1, 10))
        if react == 4:
            k4 = str
            while k4 != "play":
                print("Wants to play")
                k4 = input("What to do ? ")
                print("has played enough !")
            time.sleep(random.randint(1, 10))

if __name__ == "__main__":
    main()
    choice_a()
    choice_c()
    reactions()