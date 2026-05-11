import random
import time
import sys
from pathlib import Path
from colorama import Fore, Style, init
from playsound import playsound
from trial import Shared
#Paths for voicelines
base = Path(__file__).resolve().parent
kafka_fua = base.parent / "data" / "assets" / "kafkafua.mp3"
mydei = base.parent / "data" / "assets" / "mydei.mp3"
blade_ult = base.parent / "data" / "assets" / "blade.mp3"
blade_fua = base.parent / "data" / "assets" / "bladefua.mp3"
sparxie = base.parent / "data" / "assets" / "sparxie.mp3"
hyacine = base.parent / "data" / "assets" / "Hyacine.mp3"
kafka_ult = base.parent / "data" / "assets" / "kafka.mp3"

#Method for slow typing
def slow(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

#initializing colorama
init()

#Shared across all characters methods
class Effects():
    #poison effect
    def poison(self):
        self.poisoned -= 1
        self.hp -= self.poisoned_dmg
        print(f"{Fore.MAGENTA}Poison effect! {Style.RESET_ALL} lost {self.poisoned_dmg} hp")

    #energy cap so it does not exceed 100
    def energy_cap(self, er):
       if self.energy < 100:
           self.energy += er
       if self.energy > 100:
         self.energy = 100

    #hp cap do it does not exceed max hp
    def hp_cap(self):
        if self.hp > self.fullhp:
            self.hp = self.fullhp

    def shield(self,dmg):
        absorbed = min(self.shield, dmg)
        self.shield -= absorbed
        remaining = dmg - absorbed
        self.hp -= remaining
        

""" 
Each character has has the same 5 methods:
    -normal_attack() to perform a normal attack
    -skill() to perform a skill
    -ultimate() to perform the ultimate
    -diplay_info() to display current character info
    -take_damage() to take damage
Used mydei as an example undeneath, follow the comments.
For in-depth details about characters skill please read the Tutorial.txt file.
All characters inherit from the effects class.
 """

class Mydei(Effects,Shared):
    def __init__(self, hp = 5000):
        Shared.__init__(self,hp)
        self.name = "Mydei"
        self.skill_name = "Deaths are Legion, Regrets are None"
        self.ultimate_name = "Throne of Bones"
        self.na_name = "Vow of voyage"
        self.vendetta = 1
    
    #take damage method
    def take_damage(self, dmg, opp=None):
        if self.shield > 0:
            self.shield(dmg)
        else: self.hp -= dmg
        if self.hp <= 0 and self.vendetta == 1:
            self.vendetta = 0
            self.hp = round(self.fullhp * 0.3)
            print(f"You died. Consumed Vendetta token to get revived with {Fore.GREEN}{self.hp}{Style.RESET_ALL}")
    
    #normal attack method
    def normal_attack(self, opp):
        dmg = round(self.fullhp * 0.25)
        if self.skill_points < 5:
            self.skill_points += 1
        self.energy_cap(30)
        print(f"[Normal Attack]: {self.na_name} => {dmg}💥")
        opp.take_damage(dmg,self)
        return 1
        
    #Skill method
    def skill(self, opp):
        if self.skill_points > 0:
            dmg = round(self.fullhp * 0.4)
            if self.hp < round(self.fullhp * 0.1):
                self.hp = 1
                print(f"[Skill]: {self.skill_name} => -99% HP, {dmg}💥")
            else:
                self.hp -= round(self.hp * 0.3)
                print(f"[Skill]: {self.skill_name} => -30% HP, {dmg}💥")
            opp.take_damage(dmg, self)
            self.skill_points -= 1
            self.energy_cap(35)
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move.\n")
            return 0  
        
    #Ultimate method
    def ultimate(self, opp):
        if self.energy == 100:
            if self.hp <= round(self.fullhp * 0.1):
                dmg = round(self.fullhp * 1)
                heal= round(self.fullhp * 0.4)
            else:
                dmg = round(self.fullhp * 0.5)
                heal= round(self.fullhp * 0.2)
            self.hp += heal
            self.hp_cap()
            self.energy = 0
            playsound(str(mydei), block = False)
            time.sleep(1)
            slow("Now accept your punishment!")
            time.sleep(1)
            print(f"[Ultimate]: {self.ultimate_name} => {dmg}💥, ➕{heal}")
            opp.take_damage(dmg, self)
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move.\n")
            return 0
        
    #Display current info
    def display_info(self):
        print(f"[PLAYER]: {self.name} | [HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL}")
        print(f"[SP]: {Fore.YELLOW}{self.skill_points}{Style.RESET_ALL} | [E]: {Fore.BLUE}{self.energy}{Style.RESET_ALL}")
        print(f"[SHIELD]: {Fore.LIGHTWHITE_EX}{self.shield}{Style.RESET_ALL}")
        print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
        print(15*"-")


class Blade(Effects,Shared):
    def __init__(self, hp = 5000):
        Shared.__init__(self,hp)
        self.name = "Blade"
        self.skill_name = "Hellscape"
        self.ultimate_name = "Death Sentence"
        self.na_name = "Shard Sword"
        self.na_name_enhanced = "Forest of swords"
        self.hellscape = 0
        self.counter = 0
        self.stack = 0
        
    def take_damage(self, dmg, opp=None):
        if self.shield > 0:
            self.shield -= dmg
            if self.shield < 0:
                self.hp += self.shield
                self.shield = 0
                self.stack += 1
                if self.stack >= 5 and opp is not None:
                    self.followup(opp)
        else: 
            self.hp -= dmg
            self.stack += 1
            if self.stack >= 5 and opp is not None:
                self.followup(opp)
      
    def normal_attack(self, opp):
        if self.hellscape == 0:
            dmg = round(self.fullhp * 0.25)
            if self.skill_points < 5:
                self.skill_points += 1
            self.energy_cap(15)
            print(f"[Normal Attack]: {self.na_name} => {dmg}💥")
            opp.take_damage(dmg, self)
        else:
            self.counter += 1
            dmg = round(self.fullhp * 0.37)
            self.take_damage(self.hp * 0.25)
            self.energy_cap(30)
            print(f"[Enhanced Normal Attack]: {self.na_name} => {dmg}💥")
            opp.take_damage(dmg, self)
            if self.counter == 3:
                print("Exited Hellscape mode!")
                self.hellscape = 0
                self.counter = 0
        return 1
    
    def followup(self, opp):
        dmg = round(self.fullhp * 0.6)
        heal = round(self.fullhp * 0.25)
        self.hp += heal
        self.hp_cap()
        self.energy_cap(25)
        opp.take_damage(dmg,self)
        playsound(str(blade_fua), block = False)
        time.sleep(1)
        slow("A vale to send you!")
        time.sleep(1)
        print(f"[Follow-up ATK]: Shuhu's Gift => {dmg}💥, ➕{heal}")
        self.stack = 0
    
    
    def skill(self, opp):
        if self.hellscape == 0:
            if self.skill_points > 0:
                self.hellscape = 1
                self.skill_points -= 1
                print("entered Hellscape mode!")
                self.normal_attack(opp)
                return 1
            else:
                print("Not enough skill points to unleash Skill! please choose a different move.\n")
                return 0  
        else: 
            print("You are in Hellscape mode! cannot perform skill again.\n")
            return 0
    
    
    def ultimate(self, opp):
        if self.energy == 100:
            if self.hp > round(self.fullhp * 0.5):
                self.stack += 1
            self.hp = round(self.fullhp * 0.5)
            dmg = round(self.fullhp * 0.9)
            self.energy = 0
            playsound(str(blade_ult), block = False)
            time.sleep(1)
            slow("Savor it for me!")
            time.sleep(1)
            print(f"[Ultimate]: {self.ultimate_name} => {dmg}💥")
            opp.take_damage(dmg,self)
            if self.stack >= 5:
                self.followup(opp)
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move.\n")
            return 0
        
    def display_info(self):
        print(f"[PLAYER]: {self.name} | [HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL}")
        print(f"[SP]: {Fore.YELLOW}{self.skill_points}{Style.RESET_ALL} | [E]: {Fore.BLUE}{self.energy}{Style.RESET_ALL}")
        print(f"[FUA-STACKS]: {Fore.LIGHTBLACK_EX}{self.stack}{Style.RESET_ALL}")
        print(f"[SHIELD]: {Fore.LIGHTWHITE_EX}{self.shield}{Style.RESET_ALL}")
        print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
        print(15*"-")

class Sparxie(Effects):
    def __init__(self, hp = 5000, atk = 1500):
        Shared.__init__(self,hp,3)
        self.name = "Sparxie"
        self.skill_name = "Bloom! Winner Takes All"
        self.ultimate_name = "Party's Wildin' and Cameras' Rollin'"
        self.na_name = "Cat Got Your Flametoungue?"
        self.punchline = 0
        self.skill_state = 0
        self.skill_counter = 0
        self.fullatk = atk
        self.atk = atk
        self.turn = 0
        
    
    #Turn counter for her talent: elation skill
    def turn_counter(self, opp):
        self.turn += 1
        if self.turn == 3:
            self.turn = 0
            dmg = round(self.atk + (self.punchline * 0.03 * self.atk))
            self.energy_cap(25)
            print(f"[Elation Skill]: Signal Overflow: The Great Encore! => {dmg}💥 through {self.punchline} Punchlines!")
            self.punchline = 0
            opp.hp -= dmg
            if opp.name == "Harmonic Choir":
                if opp.hp <= 0:
                    self.Echos = 0
                    opp.take_damage(dmg, self)
            
    
    def take_damage(self, dmg, opp=None):
        if self.shield > 0:
            self.shield(dmg)
        else: self.hp -= dmg
        
    #skill point cap
    def sp_cap(self):
        self.skill_points += 1
        if self.skill_points > 8:
            self.skill_points = 8

    def normal_attack(self, opp):
        if self.skill_state == 0:
            dmg = round(self.atk * 0.5)
            self.punchline += 2
            self.sp_cap()
            self.energy_cap(15)
            print(f"[Normal Attack]: {self.na_name} => {dmg}💥")
            opp.take_damage(dmg, self)
        else:
            dmg = round(self.atk*self.skill_counter * 0.35)
            self.skill_state = 0
            energy = 30 + self.skill_counter * 2
            self.energy_cap(energy)
            self.skill_counter = 0
            print(f"[Skill]: {self.skill_name} => {dmg}💥")
            opp.take_damage(dmg, self)
        self.turn_counter(opp)
        return 1
    
    
    def skill(self, opp):
        if self.skill_points > 0:
            self.skill_state = 1
            buff = ["Straight Fire","Unreal Banger"]
            weight = [30,70]
            print("Boom! Sparxicle's Poppin' Started!")
            while self.skill_points > 0 and self.skill_counter < 10:
                self.skill_points -= 1
                self.skill_counter += 1
                buffpick = random.choices(buff,weight)[0]
                if buffpick == "Straight Fire":
                    self.punchline += 2
                    self.sp_cap()
                    self.sp_cap()
                    print(f"Engagement Farming: {Fore.RED}Straight Fire{Style.RESET_ALL} triggered!")
                else: 
                    self.punchline += 1
                    print(f"Engagement Farming: {Fore.YELLOW}Unreal Banger{Style.RESET_ALL} triggered!")
                pick = 0
                while pick == 0:
                    try:
                        decision = int(input(f"[SP]: {self.skill_points} -- Consumed SP: ({self.skill_counter}/10)\nConsume more SP (1) or Attack (2)?: "))
                        pick = 1
                    except ValueError:
                        print("please pick a number.")
                while decision not in [1,2]:
                    try:
                        decision = int(input("Please pick a number between 1 (consume SP) or 2 (Attack) only: "))
                    except ValueError:
                        print("please pick a number.")
                while decision == 1:
                    if self.skill_points == 0 or self.skill_counter == 10:
                        try:
                            decision = int(input("Cannot consume any more Skill Points. Pick 2 to Attack: "))
                            if decision != 2:
                                raise Exception("You can only pick the number 2.")
                        except ValueError:
                            print("please pick a number.")
                        except Exception as e:
                            print(e)
                            decision = 1
                    else: break
                if decision == 2:
                    self.normal_attack(opp)
                    break
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move.\n")
            return 0  
    
    
    def ultimate(self, opp):
        if self.energy == 100:
            dmg = round(self.atk * 1.5)
            self.punchline += 5
            self.energy = 0
            playsound(str(sparxie), block = False)
            time.sleep(1)
            slow("Party 'till the end of the world!")
            time.sleep(1)
            print(f"[Ultimate]: {self.ultimate_name} => {dmg}💥")
            opp.take_damage(dmg,self)
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move.\n")
            return 0
        
    def display_info(self):
        print(f"[PLAYER]: {self.name} | [HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL} | [ATK]: {Fore.RED}{self.atk}{Style.RESET_ALL}")
        print(f"[SP]: {Fore.YELLOW}{self.skill_points}{Style.RESET_ALL} | [E]: {Fore.BLUE}{self.energy}{Style.RESET_ALL}")
        print(f"[PUNCHLINE]: {Fore.LIGHTBLACK_EX}{self.punchline}{Style.RESET_ALL}")
        print(f"[SHIELD]: {Fore.LIGHTWHITE_EX}{self.shield}{Style.RESET_ALL}")
        print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
        print(15*"-")

class Hyacine(Effects,Shared):
    def __init__(self, hp = 5500):
        Shared.__init__(self,hp)
        self.name = "Hyacine"
        self.skill_name = "Love Over The Rainbow"
        self.ultimate_name = "We Who Fly Into Twilight"
        self.na_name = "When Breeze Kisses Cirrus"
        self.fullhp_count = 0
        self.fullhpbuff = round(self.fullhp * 0.25)
        self.icafullhp = round(self.fullhp * 0.5)
        self.heal = 1000
        self.ica = 0
        self.ica_count = 0
        self.ica_hp = round(self.fullhp * 0.5)
        self.ica_attack = "Rainclouds, Time To Go!"
        
    
    #slightly changed hp_cap for hyacine: added ica
    def hp_cap(self):
        if self.hp > self.fullhp:
            self.hp = self.fullhp
        if self.ica_hp > self.icafullhp:
            self.ica_hp = self.icafullhp

    def take_damage(self, dmg, opp=None):
        if self.ica == 1:
            char = ["hyacine","ica"]
            weight = [40,60]
            attacked = random.choices(char,weight)[0]
            if attacked == "hyacine":
                if self.shield > 0:
                    self.shield(dmg)
                else: self.hp -= dmg
                print(f"Hyacine has suffered {dmg}💥")
            else: 
                self.ica_hp -= dmg
                print(f"Little Ica has suffered {dmg}💥")
                if self.ica_hp <= 0:
                    self.ica = 0
                    print("Ica has left the field.")
        else:
            if self.shield > 0:
                    self.shield(dmg)
            else: self.hp -= dmg
            
    #Special attack method for Ica
    def ica_damage(self):
        dmg = round(self.heal*0.7)
        self.ica_count -= 1
        if self.heal >= 1000:
                self.heal -= self.heal * 0.5
        return dmg
    
    def normal_attack(self, opp):
        dmg = round(self.fullhp * 0.2)
        if self.skill_points < 5:
            self.skill_points += 1
        self.energy_cap(15)
        print(f"[Normal Attack]: {self.na_name} => {dmg}💥")
        opp.take_damage(dmg, self)
        if self.ica == 1 and self.ica_count >= 1:  
            self.energy_cap(10)
            ica = self.ica_damage()
            print(f"[Ica: Normal Attack]: {self.ica_attack} => {ica}💥")
            opp.take_damage(ica, self)
        if self.fullhp_count > 0:
            self.fullhp_count -= 1
            if self.fullhp_count == 0:
                self.fullhp -= self.fullhpbuff
                self.hp_cap()
                print("HP Buff ended.")
        return 1
        
    
    def skill(self, opp):
        if self.skill_points > 0:
            heal = round(self.fullhp * 0.15)
            self.hp += heal
            self.heal += heal
            self.hp_cap()
            self.skill_points -= 1
            self.energy_cap(50)
            if self.ica == 0:
                self.ica = 1
                self.ica_hp = self.icafullhp
                print(f"[Skill]: {self.skill_name} => ➕{heal}")
                print("Summoned Little Ica!")
            else:
                 self.ica_hp += heal
                 self.heal += heal
                 self.hp_cap()
                 print(f"[Skill]: {self.skill_name} => ➕{heal} (Ica too)")
                 if self.ica_count >= 1:
                     dmg = self.ica_damage()
                     print(f"[Ica: Normal Attack]: {self.ica_attack} => {dmg}💥")
                     opp.take_damage(dmg, self)
            if self.fullhp_count > 0:
                self.fullhp_count -= 1
                if self.fullhp_count == 0:
                    self.fullhp -= self.fullhpbuff
                    self.hp_cap()
                    print("Hp Buff ended.")
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move.\n")
            return 0  
        
    
    def ultimate(self, opp):
        if self.energy == 100:
            heal= round(self.fullhp * 0.3)
            self.fullhp += self.fullhpbuff
            self.hp += heal
            self.hp_cap()
            self.heal += heal
            playsound(str(hyacine), block = False)
            time.sleep(1)
            slow("Dispel the gloom, restore the skies!")
            time.sleep(1)
            print(f"[Ultimate]: {self.ultimate_name} => ➕{heal}, new max [HP] => {self.fullhp}")
            self.fullhp_count = 3
            if self.ica == 0:
                self.ica = 1
                self.ica_hp = self.icafullhp
                print("Summoned Little Ica!")
            else:
                self.ica_hp += heal
                self.hp_cap()
                self.heal += heal
                print(f"Healed Little Ica too!")
            self.ica_count = 4
            dmg = self.ica_damage()
            print(f"[Ica: Normal Attack]: {self.ica_attack} => {dmg}💥")
            opp.take_damage(dmg, self)
            self.energy = 0          
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move.\n")
            return 0
        
    def display_info(self):
        print(f"[PLAYER]: {self.name} | [HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL}")
        print(f"[SP]: {Fore.YELLOW}{self.skill_points}{Style.RESET_ALL} | [E]: {Fore.BLUE}{self.energy}{Style.RESET_ALL}")
        if self.fullhp_count > 0:
            print(f"[HP-BUFF]: Activated ")
        else: print(f"[HP-BUFF]: Deactivated ")
        if self.ica == 1:
            print(f"[PET]: Little Ica")
            print(f"[HP]: {Fore.GREEN}{round(self.ica_hp)}{Style.RESET_ALL}")
            print(f"[Ica-SPECIAL ATK]: {Fore.LIGHTBLACK_EX}{self.ica_count}{Style.RESET_ALL}")
        print(f"[SHIELD]: {Fore.LIGHTWHITE_EX}{self.shield}{Style.RESET_ALL}")
        print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}")
        print(15*"-")

class Kafka(Effects,Shared):
    def __init__(self, hp = 4500, atk = 2000):
        Shared.__init__(self,hp)
        self.name = "Kafka"
        self.skill_name = "Caressing Moonlight"
        self.ultimate_name = "Twilight Trill"
        self.na_name = "Midnight Tumult"
        self.fua_counter = 0
        self.atk = atk
        self.fullatk = atk
       

    def take_damage(self, dmg, opp=None):
        if self.shield > 0:
            self.shield(dmg)
        else: self.hp -= dmg
        if self.atk < 2500:  # or < self.fullatk + self.fullatk * 0.25 if changes were ever done
            self.atk += self.fullatk * 0.025
            print(f"+{round(self.fullatk * 0.025)} ATK")
      
    def normal_attack(self, opp):
            dmg = round(self.atk * 0.25)
            if self.skill_points < 5:
                self.skill_points += 1
            self.energy_cap(30)
            print(f"[Normal Attack]: {self.na_name} => {dmg}💥")
            opp.take_damage(dmg, self)
            if self.fua_counter >= 1:
                self.followup(opp)
            return 1
    
    def followup(self, opp):
        self.fua_counter -= 1
        dmg = round(self.atk * 0.15)
        opp.poisoned += 2
        self.energy_cap(25)
        playsound(str(kafka_fua), block = False)
        time.sleep(1)
        slow("Stand still")
        time.sleep(1)
        print(f"[Follow-up ATK]: Gentle but Cruel => {dmg}💥\nIncreased opponent's poisoned state to {opp.poisoned}")
        opp.take_damage(dmg, self)
    
    
    def skill(self, opp):
        if self.skill_points > 0:
            dmg = round(self.atk * 0.4)
            self.skill_points -= 1
            self.energy_cap(40)
            print(f"[Skill]: {self.skill_name} => {dmg}💥")
            opp.take_damage(dmg, self)
            if opp.poisoned >= 1:
                print(f"[DOT] => {round(opp.poisoned_dmg)}💥")
                opp.take_damage(round(opp.poisoned_dmg),self)
            if self.fua_counter >= 1:
                self.followup(opp)
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move.\n")
            return 0  
            
    
    
    def ultimate(self, opp):
        if self.energy == 100:
            dmg = round(self.atk * 0.9)
            self.energy = 0
            playsound(str(kafka_ult), block = False)
            time.sleep(1)
            slow("Time to say bye.")
            time.sleep(1.5)
            slow("BOOM.")
            time.sleep(1)
            print(f"[Ultimate]: {self.ultimate_name} => {dmg}💥")
            opp.take_damage(dmg, self)
            self.fua_counter += 2
            if opp.poisoned >= 1:
                print(f"[DOT] => {round(opp.poisoned_dmg*2)}💥")
                opp.take_damage(round(opp.poisoned_dmg*2),self)
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move.\n")
            return 0
        
    def display_info(self):
        print(f"[PLAYER]: {self.name} | [HP]: {Fore.GREEN}{round(self.hp)}{Style.RESET_ALL} | [ATK]: {Fore.RED}{round(self.atk)}{Style.RESET_ALL}")
        print(f"[SP]: {Fore.YELLOW}{self.skill_points}{Style.RESET_ALL} | [E]: {Fore.BLUE}{self.energy}{Style.RESET_ALL}")
        print(f"[FUA]: {Fore.LIGHTBLACK_EX}{self.fua_counter}{Style.RESET_ALL}")
        print(f"[SHIELD]: {Fore.LIGHTWHITE_EX}{self.shield}{Style.RESET_ALL}")
        print(f"[POISON]: {Fore.MAGENTA}{self.poisoned}{Style.RESET_ALL}\n")
        print(15*"-")
