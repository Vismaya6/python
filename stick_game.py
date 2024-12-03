'''
Author:Vismaya Theresa Benny
Date:3/12/2024
game
'''
def game():
    player1=input("Enter the name of player1:")
    player2=input("Player2 name:")
    sticks=16
    print("Game started")
    remaining=sticks
    while (remaining>0):
        play1=int(input("Enter the choice of first player(1,2,3):"))
        remaining=remaining-play1
        print("Remaining=",remaining)
        if remaining==0:
            print("Player 1 Loses")
        else:("player 1 wins")
        play2=int(input("Enter the choice of player2(1,2,3):"))
        remaining=remaining-play2
        print("Remaining=",remaining)
        if remaining==0:
            print(" Player 2 loses")
        else:("player2 wins")
game()