import random
from Characters import *

#Main characters class
class Character:
    #initialization
    def __init__(self,name = "Character",skill= "Skill",ultimate= "Ultimate",na = "Normal Attack",hp = 100):
        self.name = name
        self.skill_name = skill
        self.ultimate_name = ultimate
        self.na_name = na
        self.hp = hp
        self.skill_points = 2
        self.energy = 0
        pass

    #Normal Attack method
    def normalAttack(self,ai):
        ai.hp -= 10
        self.skill_points += 1
        self.energy += 15
        if ai.hp >= 0:
            print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! The opponents hp is now: {ai.hp}")
        else: print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! The opponents hp is now: 0")
        return 1
    #Skill method
    def skill(self,ai):
        if self.skill_points > 0:
            ai.hp -= 15
            self.skill_points -= 1
            self.energy += 30
            if ai.hp >= 0:
                print(f"{self.name} unleashed their Skill: {self.skill_name} and caused 15 dmg! The opponenets hp is now: {ai.hp}")
            else: print(f"{self.name} unleashed their Skill: {self.skill_name} and caused 15 dmg! The opponents hp is now: 0")
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move: ")
            return 0
    #Ultimate method
    def ultimate(self,ai):
        if self.energy >= 100:
            ai.hp -= 40
            self.energy -= 100
            if ai.hp >= 0:
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! The opponents hp is now: {ai.hp}")
            else: print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! The opponents hp is now: 0")
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
        
   

#AI class inherits from Character class
class AI(Character):
    #Normal Aattck class: changed text output
    def normalAttack(self,opp):
        if opp.name == "Mydei":
            opp.hp -= 300
        else:
            opp.takeDamage(300,self)
        self.skill_points += 1
        self.energy += 15
        if opp.hp >= 0:
            print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! Your hp is now: {opp.hp}")
        else: 
            print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! Your hp is now: 0")
            opp.takeDamage(300)
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            if opp.name == "Mydei":
                opp.hp -= 500
            else:
                opp.takeDamage(300,self)
            self.skill_points -= 1
            self.energy += 30
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Skill: {self.skill_name} and caused 15 dmg! Your hp is now: {opp.hp}")
            else: 
                print(f"{self.name} unleashed their Skill:  {self.skill_name} and caused 15 dmg! Your hp is now: 0")
                opp.takeDamage(300)
            
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            if opp.name == "Mydei":
                opp.hp -= 300
            else:
                opp.takeDamage(300,self)
            self.energy -= 100
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! Your hp is now: {opp.hp}")
            else: 
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! Your hp is now: 0")
                opp.takeDamage(300)

    #AI random move based on available resources
    def ai_move(self,opponent):
        available = []
        proba = []

        available.append("normal")
        proba.append(30)

        if self.skill_points > 0:
            available.append("skill")
            proba.append(60)
        if self.energy >= 100:
            available.append("ultimate")
            proba.append(70)
        if "ultimate" in available and self.hp >= 40:
            proba[-1] += 30
        
        move = random.choices(available,proba)[0]

        if move == "normal":
            self.normalAttack(opponent)
        elif move == "skill":
            self.skill(opponent)
        elif move == "ultimate":
            self.ultimate(opponent)
        

mydei = Character()
char2 = AI("phainon","swipe","wrath","clap",20000)

#MAIN LOOP FOR THE GAME

"""pick = 0
while pick == 0:
    player = int(input("Please pick character corresponding to the numbers:\n1.Phainon\n2.Mydei\n3.Sparxie\n4.The Herta\n5.Dr. Ratio\n6.Acheron\n7.Jungliu\n8.Blade\n9.Kafka\n10.Himeko\n0.Random\nChoose a number: "))
    """
while mydei.hp > 0 and char2.hp > 0:
    player_move = 0
    while player_move == 0:
        print("please select your move:\n1 for normal attack\n2 for skill\n3 for ultimate")
        mydei.displayInfo(char2)
        move = int(input(f"You choose: "))
        if move == 1:
            player_move = mydei.normalAttack(char2)
        elif move == 2:
            player_move = mydei.skill(char2)
        elif move == 3 :
            player_move = mydei.ultimate(char2)
        else : print("Invalid move, try again.")
    
    if player_move == 1 and char2.hp > 0:
        char2.ai_move(mydei)

    if mydei.hp <= 0:
        print(f"Game Over! {char2.name} won! player {mydei.name} lost!")
        break
    elif char2.hp <= 0:
        print(f"Game Over! {mydei.name} won! player {char2.name} lost!")
        break


