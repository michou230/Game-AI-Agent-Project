import time
from Characters import *
from enemies import *


#MAIN LOOP FOR THE GAME

picked = 0 #FOR PLAYER CHARACTER PICK
choose = 0 #FOR PLAYER CHARACTER PICK CHECK

pick = 0 #FOR PLAYER ENEMY PICK
choice = 0  #FOR PLAYER ENEMY PICK CHECK


characters = {
    1: Mydei,
    2: Sparxie,
    3: Blade,
    4: Kafka,
    5: Hyacine
}

enemies = {
    1: Pollux,
    2: Lieutenant,
    3: Sunday
}


#LOOP TO PICK A CHARACTER 
while picked == 0:
    while choose == 0:
        try:
            player = int(input("\nPlease pick character corresponding to the numbers:\n[0].Random | [1].Mydei | [2].Sparxie | [3].Blade | [4].Kafka | [5].Hyacine\nChoose a number: "))
            choose = 1
        except ValueError:
            print("please pick a number.")
    while player not in [0,1,2,3,4,5]:
        try:
            player = int(input("Please pick a valid number: "))
        except ValueError:
            print("A number please.")
    if player == 0:
      print("\nSelecting Character. . .")
      p1 = random.choice(list(characters.values()))()
      picked = 1
      time.sleep(2)
      print(f"\nPicked the Character: {p1.name}")
      time.sleep(1)
    else: 
        p1 = characters[player]()
        picked = 1
        print(f"\nPicked the Character: {p1.name}")
        time.sleep(2)
    

#LOOP TO PICK AN ENEMY
while pick == 0:
    while choice == 0:
        try:
            enemy = int(input("\nPlease pick the enemy corresponding to the numbers:\n[0].Random | [1].Pollux | [2].Silvermane Lieutenant | [3].Harmonic Choir\nChoose a number: "))
            choice = 1
        except ValueError:
            print("please pick a number.")
    while enemy not in [0,1,2,3]:
        try:
            enemy = int(input("Please pick a valid number: "))
        except ValueError:
            print("A number please.")

    if enemy == 0:
      print("\nSelecting Enemy. . .")
      p2 = random.choice(list(enemies.values()))()
      pick = 1
      time.sleep(2)
      print(f"\nPicked the Enemy: {p2.name}")
      time.sleep(1)
      print("\nStarting battle. . .")
      time.sleep(2)
    else: 
        p2 = enemies[enemy]()
        pick = 1
        print(f"Picked the enemy: {p2.name}")
        time.sleep(2)
        print("\nStarting battle. . .")
        time.sleep(2)
    
    
# MAIN LOOP
print("\nRemember, your moves are:\n[1] for Normal Attack\n[2] for Skill\n[3] for Ultimate")
turn = 1 #Keeping track of the number of turns
while p1.hp > 0 and p2.hp > 0:
    player_move = 0 #check if player has made a valid action
    print("\t"+ 30*"=" + f"TURN {turn}" + 30*"=" + "\n")
    while player_move == 0:
        if p1.poisoned >= 1:
            p1.poison() #check if poisoned, if yes, inflict damage
        p1.display_info()
        p2.display_info()
        m = 0
        #CORRECT MOVE LOOP
        while m == 0:
            try:
                move = int(input(f"\nYou choose: "))
                if move not in [1,2,3]:
                    print("Invalid move, try again.")
                else: m = 1
            except ValueError:
                print("Only numbers please.")
        print("\n")
        if move == 1:
            player_move = p1.normal_attack(p2)
        elif move == 2:
            player_move = p1.skill(p2)
        elif move == 3 :
            player_move = p1.ultimate(p2) 
    
    #AI TURN ONLY IF THE PLAYER HAS MADE A VALID MOVE AND IS ALIVE
    if player_move == 1 and p2.hp > 0:
        turn += 1
        if p2.poisoned >= 1:
            p2.poison(p1) #check if poisoned, if yes, inflict damage
        print("\nOpponent thinking. . .\n")
        time.sleep(2)
        p2.ai_move(p1)
        print("\n")
        time.sleep(2)


    if p1.hp == 0 and p2.hp == 0:
        print(f"Game Over! That was a tie!")
    elif p1.hp <= 0:
        print(f"Game Over! {p2.name} won! player {p1.name} lost!")
        break
    elif p2.hp <= 0:
        print(f"Game Over! {p1.name} won! opponent {p2.name} lost!")
        break
    


