def roshambo ():
    import time
    import math
    from random import randint
    wins = 0
    losses = 0
    ties = 0
    win = "You Win!"
    lose = "You lose!"
    tie = "It's a tie!"
    player = raw_input("Please choose paper, scissors, or rock!\n").lower()
    if player not in ("paper", "scissors", "rock"):
        print ("Please make a valid choice.")
        roshambo ()
    else:
        print ("You chose " + player +"!")
        time.sleep(1.5)
    comp = randint (1, 3)
    if player == "paper":
        if comp == 1:
            print (tie)
            ties += 1
        elif comp == 2:
            print (lose)
            losses += 1
        else:
            print win
            wins += 1
    elif player == "scissors":
        if comp == 1:
            print (win)
            wins += 1
        elif comp == 2:
            print (tie)
            ties += 1
        else:
            print (lose)
            losses += 1
    elif player == "rock":
        if comp == 1:
            print (lose)
            losses += 1
        if comp == 2:
            print (win)
            wins += 1
        else:
            print (tie)
            ties += 1
    time.sleep(1)
    again = raw_input("Want to play again?\n").lower()
    if again == "yes" or again == "y":
        roshambo()
    else:
        print ("Thanks for playing! You won " + str(wins) + " games, " + "you lost " + str(losses) + " games, and you had " + str(ties) + "ties!")
roshambo()
