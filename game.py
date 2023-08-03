from random import randrange
random_place = randrange(0, 8)
question = print("do you want to play x o game [y/n]")
game_playground = []
counter = 0 

def initializing_game():
    
    answer = input("y" ,"n")    
    if answer == "y":
        print ("chose x or o")
        player_one = input("user_choice")
        if player_one == "o" or "x":
            if player_one == "o":        
                computer_side = "x"
            else:
                computer_side = "o"
    else:
        print("thank you")


def play(computer_side , user_side ):
    first= print("do you want to play first[y/n]")
    yup = input(first)
    if yup == "y" or "n":
        if yup == "y":
            user_side , place = input("please take your first move and the place ").split()
            game_playground.insert(user_side , place)
            if game_playground[random_place] ==  " ":
                computer_side = game_playground.insert(computer_side , random_place)


def play_ground():

