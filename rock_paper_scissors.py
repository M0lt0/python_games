import random

def play():
    user = input("'r' for rock 'p' for paper 's' for scissors: ")
    computer = random.choice(['r', 'p','s'])

    if user == computer:
        return "it's \n a tie"
    if win(user , computer):
        return "you won!"
    
    return "you lost "    
    

def win(player , opponent ):
        
        if (player == "r" and opponent == "s" ) or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
            return True
        
print(play())