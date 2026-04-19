from trial import AI
from colorama import Fore, Style, init
import random
import time

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
            print(f"{self.name} [Skill]: {self.skill_name} => Stole ➕{dmg}.")
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
            

class Sunday(AI):
    def __init__(self, hp = 10000, atk = 1500):
        self.hp = hp
        self.atk = atk
        self.fullatk = atk
        self.name = "Harmonic Choir"
        self.p2_skill_name = "Tempestoso"
        self.p3_ultimate_name = "Im Anfang war die Tat"
        self.p2_ultimate_name = "Come Un Sogno"
        self.p2_na_name = "Maestoso"
        self.Echoes = 0
        self.echo1hp = 0
        self.echo2hp = 0
        self.echofullhp = round(self.hp*0.1)
        self.fullhp = hp
        self.poisoned = 0
        self.phase = 0
        self.count = 1
        self.poisoned_dmg = self.fullhp * 0.05
        self.skill_points = 2
        self.energy = 0
        pass
        
    #Normal Aattck class: changed text output
    def normalAttack(self,opp):
        if self.phase == 0:
            dmg = round(self.atk*0.2)
            print(f"{self.name} [Normal Attack]: {self.p2_na_name}=> {dmg}💥")
            opp.takeDamage(dmg,self)
            self.skill_points += 1
            self.energy += 20
        else:
            match(self.count):
                case 1:
                    print("On the first day, grant Truth..")
                    self.count += 1
                case 2:
                    print("On the second day, grant Calendar..")
                    self.count += 1
                case 3:
                    print("On the third day, grant Language..")
                    self.count += 1
                case 4:
                    print("On the fourth day, grant Value..")
                    self.count += 1
                case 5:
                    print("On the fifth day, grant Rules..")
                    self.count += 1
                case 6:
                    print("On the sixth day, grant Meaning..")
                    self.count += 1
                case 7:
                    print("On the Seventh day, grant Dignity.. About to witness Im Anfang war die Tat!")
                    self.count += 1
                case 8:
                    dmg = self.atk * 4
                    print(f"{self.name} [Ultimate]: {self.p3_ultimate_name} => {dmg}💥")
                    opp.takeDamage(dmg,self)
                    self.count = 1


        
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            dmg = round(self.atk*0.5)
            print(f"{self.name} [Skill]: {self.p2_skill_name}=> {dmg}💥")
            opp.takeDamage(dmg,self)
            self.skill_points -= 1
            self.energy += 50
            
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            self.energy -= 100
        if self.phase == 0:
                print(f"{self.name} [Ultimate]: {self.p2_ultimate_name} and summoned his Echoes!")
                if self.Echoes == 0:
                    self.Echoes = 1
                    self.echo1hp = self.echofullhp
                    self.echo2hp = self.echofullhp
                    self.atk += round(self.fullatk*0.2)
                else:
                    if self.echo1hp <= 0:
                        self.echo1hp = self.echofullhp
                        self.atk += round(self.fullatk*0.1)
                    else: self.echo1hp = self.echofullhp
                    if self.echo2hp <= 0:
                        self.echo2hp = self.echofullhp
                        self.atk += round(self.fullatk*0.1)
                    else: self.echo2hp = self.echofullhp
                    

    def takeDamage(self,dmg,opp):
        if self.phase == 0:
            if self.Echoes == 1:
                char = ["sunday"]
                weight = [10]
                if self.echo1hp > 0:
                    char.append("echo1")
                    weight.append(45)
                if self.echo2hp > 0:
                    char.append("echo2")
                    weight.append(45)
                attacked = random.choices(char,weight)[0]
                if attacked == "echo1":
                    self.echo1hp -= dmg
                    print(f"[ECHO 1] took the damage!")
                    if self.echo1hp < 0:
                        weight.pop()
                        char.remove("echo1")
                        opp.hp += 1000
                        opp.hpCap()
                        print("[ECHO 1]: Left the field. ➕1000")
                        self.atk -= round(self.fullatk*0.1)
                        if self.echo2hp <= 0:
                            self.Echoes = 0     
                elif attacked == "echo2": 
                    self.echo2hp -= dmg
                    print((f"[ECHO 2] took the damage!"))
                    if self.echo2hp < 0:
                        weight.pop()
                        char.remove("echo2")
                        opp.hp += 1000
                        opp.hpCap()
                        print("[ECHO 2]: Left the field. ➕1000")
                        self.atk -= round(self.fullatk*0.1)
                        if self.echo1hp <= 0:
                            self.Echoes = 0  
                else:
                    print("[SUNDAY] took the damage!")
                    self.hp -= dmg
                    self.Echoes = 0
                    self.echo1hp = 0
                    self.echo2hp = 0
                    if "echo1" in char:
                        char.remove("echo1")
                        print("[ECHO 1]: Left the field.")
                        self.atk -= round(self.fullatk*0.1)
                        opp.hp += 1000
                        opp.hpCap()
                    if "echo2" in char:
                        char.remove("echo2")
                        print("[ECHO 2]: Left the field.")
                        self.atk -= round(self.fullatk*0.1)
                        opp.hp += 1000
                        opp.hpCap() 
                    for w in weight:
                        if w == 80:
                            weight.remove(w)
            else: 
                self.hp -= dmg
                if self.hp <= 0:
                    self.poisoned = 0
                    time.sleep(3)
                    print("\nAll the work of creation has been completed..")
                    time.sleep(3)
                    print("The inevitable day has arrived..")
                    time.sleep(3)
                    print("The Embryo of Philosophy..")
                    time.sleep(3)
                    print("WILL RESHAPE FOR US ALL OF REALITY!\n")
                    self.phase = 1
                    self.hp = 20000
                    time.sleep(2)
                    print("The boss has transformed to its second phase!\n")
                    opp.hp += 1500
                    opp.hpCap()
                    print("➕ 1500")
                    self.energy = 0
                    self.skill_points = 0        
        else:
            reduction = round(dmg*0.3)
            self.hp -= reduction
            shield = round(dmg*0.5)
            opp.shield += shield
            print(f"[Embryo of Philosophy]: Reduced damage taken to {reduction}💥, 🛡️ {shield}")
            print(f"[SHIELD]: accumulated {opp.shield}")


    def displayInfo(self):
         print(f"[ENEMY]: {self.name}\n[HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL} | [ATK]: {Fore.RED}{round(self.atk)}{Style.RESET_ALL}")
         print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
         if self.echo1hp > 0:
            print(f"[ECHO 1]: {Fore.GREEN}{self.echo1hp}{Style.RESET_ALL}")
         if self.echo2hp > 0:
            print(f"[ECHO 2]: {Fore.GREEN}{self.echo2hp}{Style.RESET_ALL}")
         print(15*"-")
            