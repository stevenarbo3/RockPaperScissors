import random as rand

def play():
    userPlay = input("Pick Rock (R), Paper (P), or Scissors (S): ")
    compPlay = rand.choice(['R','P','S'])
    
    print(winner(userPlay, compPlay))
    
    playAgain = input("Want to play again? (Y) or (N): ")
    if (playAgain == 'Y'):
        print("Ok let's go!")
        play()
    else:
        print("Ok see you next time")

def winner(user, comp):
    if (user == comp):
        return ("You Tied!")
    
    if (user == 'R' and comp == 'S') or (user == 'P' and comp == 'R') or (user == 'S' and comp == 'P'):
        return ("You won!")
    else:
        return ("You lost :(")
    
play()