import random
from tkinter import *
from tkinter import ttk


def computer_turn(y):
    x = 1
    y = int(input("please  enter a number [1 : ] :"))
    guess =  random.randint(x,y)
    iteration = " "
    while iteration != "c":
        iteration =input(f"is the number {guess} is high [h] , low [l] , or correct [c] ")
        if iteration == "h":
            guess = random.randint(1 , y) - 1
        elif iteration == "l":
            guess = guess = random.randint(1 , y) + 1
    
    print(f"the computer have guessed your number {guess} right ")

        


computer_turn(100)
