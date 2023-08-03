import random
random = random.randint(0 , 99)
counter = 0

while counter < 10:
  counter += 1
  guess = int(input("please enter your guess: "))
  
  
  if (guess) == random:
    print("you have guessed right") 
    break
  elif int(guess) > random:
      print(f"you enter a bigger number , you have {10- counter} trys  please try again: ")
      
  elif int(guess) < random:
      print(f"you enter a smaller number ,you have {10 - counter} trys please try again: ")
      
  elif counter == 10:
      print("you are a loser")


  


