from trial import AI
from colorama import Fore, Style, init

init()
class Pollux(AI):
    def __init__(self, hp = 20000):
        self.hp = hp
        self.name = "Pollux"
        self.skill_name = "To Die in Aromatic Pain"
        self.ultimate_name = "To Bury the Slumbered"
        self.na_name = "To Stay the Fallen"
        self.fullhp = hp
        self.poisoned = 0
        self.poisoned_dmg = self.fullhp * 0.05
        self.skill_points = 2
        self.energy = 0
        pass
        
    #Normal Aattck class: changed text output
    def normalAttack(self,opp):
        dmg = round(self.fullhp*0.01)
        print(f"{self.name} [Normal Attack]: {self.na_name}=> {dmg}💥")
        opp.takeDamage(dmg,self)
        self.skill_points += 1
        self.energy += 15
        
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            dmg = round(self.fullhp*0.05)
            self.hp += round(dmg)
            print(f"{self.name} [Skill]: {self.skill_name} => {dmg}💥, ➕{dmg}")
            opp.takeDamage(dmg,self)
            self.skill_points -= 1
            self.energy += 30
            
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            self.hp += self.fullhp*0.1
            opp.poisoned += 2
            self.energy -= 100
            print(f"{self.name} [Ultimate]: {self.ultimate_name} => ➕ {self.fullhp*0.1}  HP! You've been poisoned!")
            
    def takeDamage(self,dmg,opp=None):
        self.hp -= dmg

    def displayInfo(self):
         print(f"[ENEMY]: {self.name}\n[HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL}")
         print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
         print(15*"-")

class Lieutenant(AI):
    def __init__(self, hp = 10000, atk = 1000):
        self.hp = hp
        self.atk = atk
        self.name = "Silvermane Lieutenant"
        self.skill_name = "Pierce"
        self.ultimate_name = "Shield Reflect"
        self.na_name = "Assault"
        self.fullhp = hp
        self.poisoned = 0
        self.reflection = 0
        self.poisoned_dmg = self.fullhp * 0.05
        self.skill_points = 2
        self.energy = 0
        pass
        
    #Normal Aattck class: changed text output
    def normalAttack(self,opp):
        dmg = round(self.atk*0.3)
        print(f"{self.name} [Normal Attack]: {self.na_name}=> {dmg}💥")
        opp.takeDamage(dmg,self)
        self.skill_points += 1
        self.energy += 20
        
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            dmg = round(self.atk*0.7)
            print(f"{self.name} [Skill]: {self.skill_name}=> {dmg}💥")
            opp.takeDamage(dmg,self)
            self.skill_points -= 1
            self.energy += 50
            
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            self.energy -= 100
            print(f"{self.name} [Ultimate]: {self.ultimate_name} and activated it!")
            self.reflection += 3

    def takeDamage(self,dmg,opp):
        self.hp -= dmg
        if self.reflection >= 1:
            self.reflection -= 1
            self.hp += round(dmg*0.20)
            atk = round(self.atk*0.20)
            print(f"{Fore.LIGHTBLACK_EX}[Shield Reflection]{Style.RESET_ALL} => {atk}💥, ➕ {round(dmg*0.2)}")
            opp.takeDamage(atk,self)

    def displayInfo(self):
         print(f"[ENEMY]: {self.name}\n[HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL} | [ATK]: {Fore.RED}{round(self.atk)}{Style.RESET_ALL}")
         print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
         print(f"[SHIELD REFLECTION]: {Fore.LIGHTBLACK_EX}{self.reflection}{Style.RESET_ALL}")
         print(15*"-")
            