import random

class Character:
    
    def __init__(self,name = "Character",skill= "Skill",ultimate= "Ultimate",na = "Normal Attack",hp = 100):
        self.name = name
        self.skill_name = skill
        self.ultimate_name = ultimate
        self.na_name = na
        self.hp = hp
        self.skill_points = 2
        self.energy = 0
        pass

    def normalAttack(self,ai):
        ai.hp -= 10
        self.skill_points += 1
        self.energy += 15
        if ai.hp >= 0:
            print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! The opponenets hp is now: {ai.hp}")
        else: print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! The opponents hp is now: 0")
        return 1

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

class AI(Character):

    def normalAttack(self,opp):
        opp.hp -= 10
        self.skill_points += 1
        self.energy += 15
        if opp.hp >= 0:
            print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! Your hp is now: {opp.hp}")
        else: print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg! Your hp is now: 0")
        

    def skill(self,opp):
        if self.skill_points > 0:
            opp.hp -= 15
            self.skill_points -= 1
            self.energy += 30
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Skill: {self.skill_name} and caused 15 dmg! Your hp is now: {opp.hp}")
            else: print(f"{self.name} unleashed their Skill:  {self.skill_name} and caused 15 dmg! Your hp is now: 0")
            

    def ultimate(self,opp):
        if self.energy >= 100:
            opp.hp -= 40
            self.energy -= 100
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! Your hp is now: {opp.hp}")
            else: print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! The opponents hp is now: 0")


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
        

char1 = Character("mydei","roar","vanish","fang")
char2 = AI("phainon","swipe","wrath","clap")

while char1.hp > 0 and char2.hp > 0:
    player_move = 0
    while player_move == 0:
        move = int(input(f"please select your move:\n1 for normal attack\n2 for skill\n3 for ultimate\ncurrent skill points are {char1.skill_points}\ncurrent energy is {char1.energy}"))
        if char1.hp >= 0:
            print(f"current hp is {char1.hp} and opponents is {char2.hp}\n\n")
        else: print(f"current hp is 0 and opponents is {char2.hp}\n\n")
        if move == 1:
            char1.normalAttack(char2)
            player_move = 1
        elif move == 2:
            player_move = char1.skill(char2)
        elif move == 3 :
            player_move = char1.ultimate(char2)
        else : print("Invalid move, try again: ")
    
    if player_move == 1 and char2.hp > 0:
        char2.ai_move(char1)

    if char1.hp <= 0:
        print(f"Game Over! {char2.name} won! player {char1.name} lost!")
        break
    elif char2.hp <= 0:
        print(f"Game Over! {char1.name} won! player {char2.name} lost!")
        break


