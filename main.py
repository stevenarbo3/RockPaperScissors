import random as rand

userWins, compWins = 0, 0
wins = (userWins, compWins)

def play(wins):
    
    print("Welcome to Rock, Paper, Scissors")
    userPlay = ""
    
    while (userPlay != 'R' and userPlay != 'P' and userPlay != 'S'):
        userPlay = input("Pick Rock (R), Paper (P), or Scissors (S): ")
    
    compPlay = rand.choice(['R','P','S'])
    
    wins = winner(userPlay, compPlay, wins[0], wins[1])
    
    print(f"In this round, you have {wins[0]} win(s) and the computer has {wins[1]} win(s)")
    
    if (wins[0] > wins[1]):
        print("Keep it up!")
    elif (wins[0] < wins[1]):
        print("Step it up")
    else:
        print("Somethings gotta give, Jim")
    
    playAgain = input("Want to play again? (Y) or (N): ")
    if (playAgain == 'Y'):
        print("Ok let's go!")
        play(wins)
    else:
        print("Ok, see you next time")

def winner(user, comp, userWins, compWins):
    if (user == comp):
        print("You Tied!")
        return (userWins, compWins)
    
    if (user == 'R' and comp == 'S') or (user == 'P' and comp == 'R') or (user == 'S' and comp == 'P'):
        if (user == 'R'):
            print("Rock beats scissors!")
        elif (user == 'P'):
            print("Paper beats rock!")
        else:
            print("Scissors beats paper!")
            
        userWins += 1
        print ("You won!")
    else:
        if (user == 'R'):
            print("Paper beats rock!")
        elif (user == 'P'):
            print("Scissors beats paper!")
        else:
            print("Rock beats scissors!")
        
        compWins += 1
        print ("You lost :(")
        
    return (userWins, compWins)
    
play(wins)