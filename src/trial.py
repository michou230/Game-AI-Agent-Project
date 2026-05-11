import random
from colorama import Fore, Style, init

#THIS FILE ONLY HOLDS THE BASIC CHARACTER/AI MOVES WHICH IS THE BASE IDEA OF THE GAMEPLAY.
init()

class Shared():
    def __init__(self, hp,sp = 2):
        self.hp = hp
        self.fullhp = hp
        self.shield = 0
        self.energy = 0
        self.skill_points = sp
        self.poisoned = 0
        self.poisoned_dmg = self.fullhp * 0.05
        pass

class Character:
    #initialization
    def __init__(self,name = "Character",na = "Normal Attack",skill= "Skill",ultimate= "Ultimate",hp = 100):
        self.name = name
        self.skill_name = skill
        self.ultimate_name = ultimate
        self.na_name = na
        self.hp = hp
        self.fullhp = hp
        self.skill_points = 2
        self.energy = 0
        pass

    #Normal Attack method
    def normal_attack(self,ai):
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
    def __init__(self, na = "Normal Attack", name = "Character",skill= "Skill",ultimate= "Ultimate",hp = 100, atk = 1000):
        super().__init__(name,skill,ultimate,na,hp)
        self.atk = atk
        self.poisoned = 0
        self.poisoned_dmg = self.fullhp*0.05
        pass

    def poison(self,opp):
        self.poisoned -= 1
        self.hp -= self.poisoned_dmg
        print(f"[POISON] => {Fore.MAGENTA}{round(self.poisoned_dmg)}{Style.RESET_ALL}💥")
        if self.name == "Harmonic Choir":
                if self.hp <= 0:
                    self.Echos = 0
                    self.take_damage(self.poisoned_dmg,opp)
        
    #Normal Attack class: changed text output
    def normal_attack(self,opp):
        print(f"{self.name} unleashed their Normal Attack: {self.na_name} and caused 10 dmg!")
        opp.take_damage(self.atk*0.2,self)
        self.skill_points += 1
        self.energy += 15
        
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            if opp.name == "Mydei":
                opp.hp -= self.atk * 0.6
            else:
                opp.take_damage(self.atk * 0.6,self)
            self.skill_points -= 1
            self.energy += 30
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Skill: {self.skill_name} and caused 15 dmg! Your hp is now: {opp.hp}")
            else: 
                print(f"{self.name} unleashed their Skill:  {self.skill_name} and caused 15 dmg! Your hp is now: 0")
                opp.take_damage(300)
            
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            if opp.name == "Mydei":
                opp.hp -= 300
            else:
                opp.take_damage(300,self)
            self.energy -= 100
            if opp.hp >= 0:
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! Your hp is now: {opp.hp}")
            else: 
                print(f"{self.name} unleashed their Ultimate: {self.ultimate_name} and caused 40 dmg! Your hp is now: 0")
                opp.take_damage(300)

    #New: utility-based + probability AI
    def ai_move(self, opponent):

        utilities = {}

        # Normal Attack
        normal_score = 5

        if self.skill_points == 0:
            normal_score += 5

        utilities["normal"] = normal_score


        # Skill
        if self.skill_points > 0:
            skill_score = 5

            if self.hp < self.fullhp * 0.5:
                skill_score += 7

            utilities["skill"] = skill_score


        # Ultimate
        if self.energy >= 100:
            ult_score = 50

            if self.hp < self.fullhp * 0.4:
                ult_score += 33

            utilities["ultimate"] = ult_score

        actions = list(utilities.keys())
        weights = list(utilities.values())
        move = random.choices(actions, weights=weights)[0]

        if move == "normal":
            self.normal_attack(opponent)

        elif move == "skill":
            self.skill(opponent)

        elif move == "ultimate":
            self.ultimate(opponent)
    
    #Previous: probabilistic AI
    """#AI random move based on available resources
    def ai_move(self,opponent):
        available = []
        proba = []

        available.append("normal")
        proba.append(20)

        if self.skill_points > 0:
            available.append("skill")
            proba.append(30)
        if self.energy >= 100:
            available.append("ultimate")
            proba.append(50)
            if self.hp <= self.fullhp*0.4:
                proba[-1] += 100
        
        move = random.choices(available,proba)[0]

        if move == "normal":
            self.normal_attack(opponent)
        elif move == "skill":
            self.skill(opponent)
        elif move == "ultimate":
            self.ultimate(opponent)"""