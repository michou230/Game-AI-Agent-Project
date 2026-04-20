
from Characters import *
from enemies import *
import time



#MAIN LOOP FOR THE GAME

p = 0
c = 0

pick = 0
choice = 0
tab = ["Mydei","Sparxie","Hyacine","Blade","Kafka"]
tab2 = ["Pollux","Lieutenant","Sunday"]
while p == 0:
    while c == 0:
        try:
            player = int(input("\nPlease pick character corresponding to the numbers:\n[0].Random | [1].Mydei | [2].Sparxie | [3].Blade | [4].Kafka | [5].Hyacine\nChoose a number: "))
            c = 1
        except ValueError:
            print("please pick a number.")
    while player not in [0,1,2,3,4,5]:
        try:
            player = int(input("Please pick a valid number: "))
        except ValueError:
            print("A number please.")
    match(player):
        case 0:
            char = random.choice(tab)
            match(char):
                case "Mydei":
                    p1 = Mydei()
                    print(f"Picked the Character {p1.name}")
                    p = 1
                case "Kafka":
                    p1 = Kafka()
                    print(f"Picked the Character {p1.name}")
                    p = 1
                case "Hyacine":
                    p1 = Hyacine()
                    print(f"Picked the Character {p1.name}")
                    p = 1
                case "Sparxie":
                    p1 = Sparxie()
                    print(f"Picked the Character {p1.name}")
                    p = 1
                case "Blade":
                    p1 = Blade()
                    print(f"Picked the Character {p1.name}")
                    p = 1
        case 1:
            p1 = Mydei()
            print(f"Picked the Character {p1.name}")
            p = 1
        case 2:
            p1 = Sparxie()
            print(f"Picked the Character {p1.name}")
            p = 1
        case 3:
            p1 = Blade()
            print(f"Picked the Character {p1.name}")
            p = 1
        case 4:
            p1 = Kafka()
            print(f"Picked the Character {p1.name}")
            p = 1
        case 5:
            p1 = Hyacine()
            print(f"Picked the Character {p1.name}")
            p = 1

    
while pick == 0:
    while choice == 0:
        try:
            player = int(input("\nPlease pick the enemy corresponding to the numbers:\n[0].Random | [1].Pollux | [2].Silvermane Lieutenant | [3].Harmonic Choir\nChoose a number: "))
            choice = 1
        except ValueError:
            print("please pick a number.")
    while player not in [0,1,2,3]:
        try:
            player = int(input("Please pick a valid number: "))
        except ValueError:
            print("A number please.")
    match(player):
        case 0:
            char = random.choice(tab2)
            match(char):
                case "Pollux":
                    p2 = Pollux()
                    print(f"Picked the enemy {p2.name}")
                    pick = 1
                case "Lieutenant":
                    p2 = Lieutenant()
                    print(f"Picked the enmey {p2.name}")
                    pick = 1
                case "Sunday":
                    p2 = Sunday()
                    print(f"Picked the enemy {p2.name}")
                    pick = 1
        case 1:
            p2 = Pollux()
            print(f"Picked the enemy {p2.name}")
            pick = 1
        case 2:
            p2 = Lieutenant()
            print(f"Picked the enmey {p2.name}")
            pick = 1
        case 3:
            p2 = Sunday()
            print(f"Picked the enemy {p2.name}")
            pick = 1

    
print("\nRemember, your moves are:\n[1] for Normal Attack\n[2] for Skill\n[3] for Ultimate")
turn = 1
while p1.hp > 0 and p2.hp > 0:
    player_move = 0
    print("\t"+ 30*"=" + f"TURN {turn}" + 30*"=" + "\n")
    while player_move == 0:
        if p1.poisoned >= 1:
            p1.Poison()
        turn += 1
        p1.displayInfo()
        p2.displayInfo()
        m = 0
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
            player_move = p1.normalAttack(p2)
        elif move == 2:
            player_move = p1.skill(p2)
        elif move == 3 :
            player_move = p1.ultimate(p2) 
    
    if player_move == 1 and p2.hp > 0:
        if p2.poisoned >= 1:
            p2.Poison()
        print("\nOpponent thinking. . .\n")
        time.sleep(2)
        p2.ai_move(p1)
        print("\n")
        time.sleep(2)

    if p1.hp <= 0:
        print(f"Game Over! {p2.name} won! player {p1.name} lost!")
        break
    elif p2.hp <= 0:
        print(f"Game Over! {p1.name} won! opponent {p2.name} lost!")
        break


