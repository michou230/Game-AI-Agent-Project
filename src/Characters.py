import random
from maincode import Character

class Poisoned():
    def Poison(self):
        if self.poisoned == 0:
            self.poisoned == 3
            print(f"You've been Poisoned for 3 turns!")
        else: 
            self.poisoned -= 1
            self.hp -= self.poisoned_dmg
            print(f"Poison effect! lost {self.poisoned_dmg} hp")

class Mydei(Poisoned):
    def __init__(self, hp = 4000):
        self.name = "Mydei"
        self.skill_name = "Deaths are Legion, Regrets are None"
        self.ultimate_name = "Throne of Bones"
        self.na_name = "Vow of voyage"
        self.hp = hp
        self.poisoned = 0
        self.poisoned_dmg = self.fullhp * 0.05
        self.fullhp = hp
        self.vendetta = 1
        self.skill_points = 2
        self.energy = 0
    
    def hpCap(self):
        if self.hp > self.fullhp:
            self.hp = self.fullhp

    def energyCap(self):
        if self.energy > 100:
            self.energy = 100
    
    def takeDamage(self,dmg,opp=None):
        self.hp -= dmg
        if self.hp <= 0 and self.vendetta == 1:
            self.vendetta = 0
            self.hp = round(self.fullhp*30/100)
            print(f"Mydei has died and consumed his Vendetta token to get revived! restored hp to {self.hp}")
    
    def normalAttack(self,opp):
        dmg = round(self.fullhp*25/100)
        opp.hp -= dmg
        if self.skill_points < 5:
            self.skill_points += 1
        if self.energy < 100:
            self.energy += 15
            self.energyCap()
        if opp.hp >= 0:
            print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
        else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        return 1
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            dmg = round(self.fullhp*60/100)
            if self.hp < round(self.fullhp*10/100):
                self.hp = 1
                opp.hp -= dmg
                self.skill_points -= 1
                if self.energy < 100:
                    self.energy += 50
                    self.energyCap()
                if opp.hp >= 0:
                    print(f"you consumed all of your remaining hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"you consumed all of your remaining hp and unleashed your Skill:  {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            else: 
                self.hp -= round(self.hp*35/100)
                opp.hp -= dmg
                self.skill_points -= 1
                if self.energy < 100:
                    self.energy += 50
                    self.energyCap()
                if opp.hp >= 0:
                    print(f"you consumed 35% of your current hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"you consumed 35% of your current hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move: ")
            return 0  
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy == 100:
            if self.hp <= round(self.fullhp*10/100):
                dmg = round(self.fullhp*160/100)
                heal= round(self.fullhp*40/100)
            else:
                dmg = round(self.fullhp*80/100)
                heal= round(self.fullhp*20/100)
            self.hp += heal
            self.hpCap()
            opp.hp -= dmg
            self.energy -= 100
            if opp.hp >= 0:
                print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while healing {heal} hp! Your hp is now {self.hp} and your opponent's hp is now: {opp.hp}")
            else: print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while healing {heal} hp! Your opponent's hp is now: 0")
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
    def displayInfo(self,opp):
        print(f"current skill points are {self.skill_points}")
        print(f"current energy is {self.energy}")
        print(f"current hp is {self.hp}")
        print(f"Opponent's hp is {opp.hp}")   


class Blade(Poisoned):
    def __init__(self, hp = 4000):
        self.name = "Blade"
        self.skill_name = "Hellscape"
        self.ultimate_name = "Death Sentence"
        self.na_name = "Shard Sword"
        self.na_name_enhanced = "Forest of swords"
        self.hellscape = 0
        self.counter = 0
        self.stack = 0
        self.poisoned = 0
        self.hp = hp
        self.poisoned_dmg = self.fullhp * 0.05
        self.fullhp = hp
        self.skill_points = 2
        self.energy = 0

    def energyCap(self):
        if self.energy > 100:
            self.energy = 100

    def hpCap(self):
        if self.hp > self.fullhp:
            self.hp = self.fullhp

    def takeDamage(self,dmg,opp=None):
        self.hp -= dmg
        self.stack += 1
        if self.stack >= 5 and opp is not None:
            self.followup(opp)
      
    def normalAttack(self,opp):
        if self.hellscape == 0:
            dmg = round(self.fullhp*25/100)
            opp.hp -= dmg
            if self.skill_points < 5:
                self.skill_points += 1
            if self.energy < 100:
                self.energy += 15
                self.energyCap()
            if opp.hp >= 0:
                print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        else:
            self.counter += 1
            dmg = round(self.fullhp*37/100)
            self.takeDamage(self.hp*25/100)
            if self.energy < 100:
                self.energy += 30
                self.energyCap()
            opp.hp -= dmg
            if opp.hp >= 0:
                print(f"You consumed 25% of your hp to unleash your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You consumed 25% of your hp to unleash your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            if self.counter == 3:
                print("Exited Hellscape mode!")
                self.hellscape = 0
                self.counter = 0
        return 1
    
    def followup(self,opp):
        dmg = round(self.fullhp*0.6)
        heal = round(self.fullhp*0.25)
        self.hp += heal
        self.hpCap()
        opp.hp -= dmg
        if self.energy < 100:
            self.energy += 25
            self.energyCap()
        print(f"Performed the Follow-up ATK: Shuhu's Gift and caused {dmg} while healing {heal}")
        self.stack = 0
    
    #Skill class: changed text output
    def skill(self,opp):
        if self.hellscape == 0:
            if self.skill_points > 0:
                self.hellscape = 1
                self.skill_points -= 1
                print("entered Hellscape mode!")
                self.normalAttack(opp)
                return 1
            else:
                print("Not enough skill points to unleash Skill! please choose a different move: ")
                return 0  
        else: 
            print("You are in Hellscape mode! cannot perform skill again.")
            return 0
    
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy == 100:
            if self.hp > round(self.fullhp*50/100):
                self.stack += 1
            self.hp = round(self.fullhp*50/100)
            dmg = round(self.fullhp*90/100)
            opp.hp -= dmg
            self.energy -= 100
            if opp.hp >= 0:
                print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while your hp has been set to {self.hp}! Your opponent's hp is now: {opp.hp}")
            else: print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while your hp has been set to {self.hp}! Your opponent's hp is now: 0")
            if self.stack >= 5:
                self.followup(opp)
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
    def displayInfo(self,opp):
        print(f"current skill points are {self.skill_points}")
        print(f"current energy is {self.energy}")
        print(f"current hp is {self.hp}")
        print(f"Opponent's hp is {opp.hp}")


class Sparxie(Poisoned):
    def __init__(self, hp = 4000, atk = 1500):
        self.name = "Sparxie"
        self.skill_name = "Bloom! Winner Takes All"
        self.ultimate_name = "Party's Wildin' and Cameras' Rollin'"
        self.na_name = "Cat Got Your Flametoungue?"
        self.punchline = 0
        self.skillState = 0
        self.skillCounter = 0
        self.poisoned_dmg = self.fullhp * 0.05
        self.hp = hp
        self.poisoned = 0
        self.atk = atk
        self.turn = 0
        self.skill_points = 3
        self.energy = 0
    
    def turnCounter(self,opp):
        self.turn += 1
        if self.turn == 3:
            self.turn = 0
            dmg = round(self.atk + (self.punchline*3*self.atk/100))
            opp.hp -= dmg
            if self.energy < 100:
                self.energy += 25
                self.energyCap()
            print(f"Performed the Elation Skill: Signal Overflow: The Great Encore! Consumed {self.punchline} Punchlines and Inflicted {dmg} dmg!")
            self.punchline = 0

    def energyCap(self):
        if self.energy > 100:
            self.energy = 100
    
    def takeDamage(self,dmg,opp=None):
        self.hp -= dmg

    def spCap(self):
        self.skill_points += 1
        if self.skill_points > 8:
            self.skill_points = 8

    def normalAttack(self,opp):
        if self.skillState == 0:
            dmg = round(self.atk*50/100)
            self.punchline += 2
            opp.hp -= dmg
            self.spCap()
            if self.energy < 100:
                self.energy += 15
                self.energyCap()
            if opp.hp >= 0:
                print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        else:
            dmg = round(self.atk*self.skillCounter*35/100)
            self.skillCounter = 0
            self.skillState = 0
            if self.energy < 100:
                self.energy += 30
                self.energyCap()
            opp.hp -= dmg
            if opp.hp >= 0:
                print(f"You unleashed your Skill Attack: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You unleashed your Skill Attack: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        self.turnCounter(opp)
        return 1
    
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            if self.skillState == 0:
                self.skillState = 1
                buff = ["Straight Fire","Unreal Banger"]
                weight = [40,60]
                while self.skill_points > 0 and self.skillCounter < 10:
                    print("Boom! Sparxicle's Poppin' Started!")
                    self.skill_points -= 1
                    self.skillCounter += 1
                    buffpick = random.choices(buff,weight)[0]
                    if buffpick == "Straight Fire":
                        self.punchline += 2
                        self.spCap()
                        self.spCap()
                        print("Engagement Farming: Straight Fire triggered!")
                    else: 
                        self.punchline += 1
                        print("Engagement Farming: Unreal Banger triggered!")
                    decision = int(input(f"Remaining Skill points {self.skill_points}--Consumed skill points (/10): {self.skillCounter}\nConsume more Skill Points (1) or Attack (2)?: "))
                    while decision not in [1,2]:
                        print("Please pick a number between 1 (consume skills) or 2 (Attack) only: ")
                        decision = int(input())
                    while decision == 1:
                        if self.skill_points == 0 or self.skillCounter == 10:
                            print("Cannot consume any more Skill Points. Pick 2 to Attack: ")
                            decision = int(input())
                        else: break
                    if decision == 2:
                        self.normalAttack(opp)
                        break
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move: ")
            return 0  
    
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy == 100:
            dmg = round(self.atk*150/100)
            self.punchline += 5
            opp.hp -= dmg
            self.energy -= 100
            if opp.hp >= 0:
                print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
    def displayInfo(self,opp):
        print(f"current skill points are {self.skill_points}")
        print(f"current energy is {self.energy}")
        print(f"current hp is {self.hp}")
        print(f"Opponent's hp is {opp.hp}")
        print(f"Punchline Count: {self.punchline}")


class Hyacine(Poisoned):
    def __init__(self, hp = 4000):
        self.name = "Hyacine"
        self.skill_name = "Love Over The Rainbow"
        self.ultimate_name = "We Who Fly Into Twilight"
        self.na_name = "When Breeze Kisses Cirrus"
        self.hp = hp
        self.fullhp = hp
        self.fullhp_count = 0
        self.fullhpbuff = round(self.fullhp *0.25)
        self.icafullhp = round(self.fullhp*0.5)
        self.heal = 1000
        self.ica = 0
        self.poisoned = 0
        self.poisoned_dmg = self.fullhp * 0.05
        self.ica_count = 0
        self.ica_hp = round(self.fullhp*0.5)
        self.ica_attack = "Rainclouds, Time To Go!"
        self.skill_points = 2
        self.energy = 0
    
    def energyCap(self):
        if self.energy > 100:
            self.energy = 100
    
    def hpCap(self):
        if self.hp > self.fullhp:
            self.hp = self.fullhp
        if self.ica_hp > self.icafullhp:
            self.ica_hp = self.icafullhp

    def takeDamage(self,dmg,opp=None):
        char = ["hyacine"]
        weight = [40]
        if self.ica == 1:
            char.append("ica")
            weight.append(60)
        attacked = random.choices(char,weight)[0]
        if attacked == "hyacine":
            self.hp -= dmg
            if self.hp > 0:
                print(f"Hyacine has suffered {dmg} dmg! Your hp is now {self.hp}")
            else: print(f"Hyacine has suffered {dmg} dmg! Your hp is now: 0")
        else: 
            self.ica_hp -= dmg
            if self.ica_hp <= 0:
                self.ica = 0
                print(f"Little Ica has suffered {dmg} dmg! his hp is now: 0")
                print("Ica has left the field.")
            else: print(f"Little Ica has suffered {dmg} dmg! his hp is now {self.ica_hp}")
            
        
    def icaDamage(self):
        dmg = round(self.heal*0.5)
        self.ica_count -= 1
        if self.heal >= 1000:
                self.heal -= self.heal * 0.5
        return dmg
    
    def normalAttack(self,opp):
        if self.ica == 0:
            dmg = round(self.fullhp*15/100)
            opp.hp -= dmg
            if self.skill_points < 5:
                self.skill_points += 1
            if self.energy < 100:
                self.energy += 15
                self.energyCap()
            if opp.hp >= 0:
                print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        else:
            dmg = round(self.fullhp*15/100) 
            opp.hp -= dmg
            if self.skill_points < 5:
                self.skill_points += 1
            if self.energy < 100:
                self.energy += 25
                self.energyCap()
            if self.ica_count >= 1:
                ica = self.icaDamage()
                opp.hp -= ica
                if opp.hp >= 0:
                    print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Little ica assisted and unleashed his Attack: {self.ica_attack} dealing {ica} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Little ica assisted and unleashed his Attack: {self.ica_attack} dealing {ica} dmg! Your opponent's hp is now: 0")
            else:
                if opp.hp >= 0:
                    print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        if self.fullhp_count > 0:
            self.fullhp_count -= 1
            if self.fullhp_count == 0:
                self.fullhp -= self.fullhpbuff
                self.hpCap()
                print("Hp Buff ended.")
        return 1
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            if self.ica == 0:
                heal = round(self.fullhp*15/100)
                self.hp += heal
                self.hpCap()
                self.ica = 1
                self.ica_hp = self.icafullhp
                self.skill_points -= 1
                if self.energy < 100:
                    self.energy += 50
                    self.energyCap()
                print(f"you unleashed your Skill: {self.skill_name} and healed {heal} hp!")
                print("Summoned Little Ica!")
            else:
                 heal = round(self.fullhp*15/100)
                 self.hp += heal
                 self.heal += heal
                 self.ica_hp += heal
                 self.heal += heal
                 self.hpCap()
                 self.skill_points -= 1
                 if self.energy < 100:
                  self.energy += 50
                  self.energyCap()
                 print(f"you unleashed your Skill: {self.skill_name} and healed both you and Little Ica by {heal} hp!")
                 if self.ica_count >= 1:
                     dmg = self.icaDamage()
                     opp.hp -= dmg
                     print(f"Little Ica performed his Attack: {self.ica_attack} dealing {dmg} dmg! {self.ica_count} attacks left!")
            if self.fullhp_count > 0:
                self.fullhp_count -= 1
                if self.fullhp_count == 0:
                    self.fullhp -= self.fullhpbuff
                    self.hpCap()
                    print("Hp Buff ended.")
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move: ")
            return 0  
        
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy == 100:
            heal= round(self.fullhp*30/100)
            self.fullhp += self.fullhpbuff
            self.hp += heal
            self.hpCap()
            self.heal += heal
            print(f"you unleashed your Ultimate: {self.ultimate_name} and healed {heal} hp while increasing your max hp to {self.fullhp} hp for 3 turns! Your hp is now {self.hp} and your opponent's hp is now: {opp.hp}")
            self.fullhp_count = 3
            if self.ica == 0:
                self.ica = 1
                self.ica_hp = self.icafullhp
                print("Summoned Little Ica!")
                self.ica_count = 4
                dmg = self.icaDamage()
                opp.hp -= dmg
                print(f"Little Ica performed his Attack: {self.ica_attack} dealing {dmg} dmg! reseted the attacks to {self.ica_count}")
            else:
                self.ica_hp += heal
                self.hpCap()
                self.heal += heal
                print(f"Healed Little Ica! his hp is now {self.ica_hp}")
                self.ica_count = 4
                dmg = self.icaDamage()
                opp.hp -= dmg
                print(f"Little Ica performed his Attack: {self.ica_attack} dealing {dmg} dmg! reseted the attacks to {self.ica_count}")
            self.energy -= 100            
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
    def displayInfo(self,opp):
        print(f"current skill points are {self.skill_points}")
        print(f"current energy is {self.energy}")
        print(f"current hp is {self.hp}")
        if self.ica == 0:
            print(f"Ica is not on the field.")
        else:
            print(f"current Ica hp is {self.ica_hp}")
        print(f"Opponent's hp is {opp.hp}") 
        if self.fullhp_count > 0:
            print("HP Buff: Activated.")
        else: print("HP Buff deactivated.")