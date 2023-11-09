import random
player1_score=0
player2_score=0
for i in range(1,11):
    print("==== ROUND -{} ====".format(i))
    player1_input=input("press enter key to roll the dice-player1")
    player1_value=random.randint(1,6)
    player2_input=input("press enter key to roll the dice-player2")
    player2_value=random.randint(1,6)
    if player1_value>player2_value:
        print("player_1 wins the round")
        player1_score+=1
    elif player2_value>player1_value:
        print("player_2 wins the round")
        player2_score+=1
    else:
        print("this round is draw")
    
if player1_score>player2_score:
    print("player_1 wins the game:", player1_score )
else:
    print("player_2 wins the game:",player2_score)

    