import random as rand

def play():
    print("Welcome to Rock, Paper, Scissors")
    userPlay = ""
    
    while (userPlay != 'R' and userPlay != 'P' and userPlay != 'S'):
        userPlay = input("Pick Rock (R), Paper (P), or Scissors (S): ")
    
    compPlay = rand.choice(['R','P','S'])
    
    print(winner(userPlay, compPlay))
    
    playAgain = input("Want to play again? (Y) or (N): ")
    if (playAgain == 'Y'):
        print("Ok let's go!")
        play()
    else:
        print("Ok, see you next time")

def winner(user, comp):
    if (user == comp):
        return ("You Tied!")
    
    if (user == 'R' and comp == 'S') or (user == 'P' and comp == 'R') or (user == 'S' and comp == 'P'):
        if (user == 'R'):
            print("Rock beats scissors!")
        elif (user == 'P'):
            print("Paper beats rock!")
        else:
            print("Scissors beats paper!")
            
        return ("You won!")
    else:
        if (user == 'R'):
            print("Paper beats rock!")
        elif (user == 'P'):
            print("Scissors beats paper!")
        else:
            print("Rock beats scissors!")
        
        return ("You lost :(")
    
play()