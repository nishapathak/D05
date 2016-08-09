#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print("Chuck walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('Chuck takes the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == "find trap door":
        print('Chuck finds trap door')
        if(count < 0):
            print('Take the slide down to the gold room.')
            gold_room() 
    


def gold_room():
    print("This room is full of gold.  How much does Chuck take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, Chuck wins!")
        exit(0)
    else:
        dead("Chuck, greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is Chuck going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take":
            dead("The bear looks at Chuck then slaps your face off.")
        elif next == "honey":
            print("The bear sniffs for the honey pot.")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. Chuck can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" and bear_moved:
            gold_room()
        elif next == "door":
            dead("The bear confuses you with a pot of honey.")
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here Chuck sees the great evil Cthulhu.")
    print("He, it, whatever stares at Chuck and Chuck goes insane.")
    print("Does Chuck flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("Chuck is in a dark room.")
    print("There is a door to your right and left.")
    print("Which one does Chuck take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("Chuck stumbles around the room until Chuck starves.")

if __name__ == '__main__':
    start()
