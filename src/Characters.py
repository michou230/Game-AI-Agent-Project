
class Mydei():
    def __init__(self, hp = 4000):
        self.name = "Mydei"
        self.skill_name = "Deaths are Legion, Regrets are None"
        self.ultimate_name = "Throne of Bones"
        self.na_name = "Vow of voyage"
        self.hp = hp
        self.fullhp = hp
        self.skill_points = 2
        self.energy = 0
        
    def normalAttack(self,opp):
        dmg = round(self.fullhp*25/100)
        opp.hp -= dmg
        self.skill_points += 1
        self.energy += 15
        if opp.hp >= 0:
            print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
        else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        return 1
        
    #Skill class: changed text output
    def skill(self,opp):
        if self.skill_points > 0:
            dmg = round(self.fullhp*45/100)
            if self.hp < round(self.hp*10/100):
                self.hp = 1
                opp.hp -= dmg
                self.skill_points -= 1
                self.energy += 50
                if opp.hp >= 0:
                    print(f"you consumed all of your remaining hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"you consumed all of your remaining hp and unleashed your Skill:  {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            else: 
                self.hp -= round(self.hp*35/100)
                opp.hp -= dmg
                self.skill_points -= 1
                self.energy += 50
                if opp.hp >= 0:
                    print(f"you consumed 35% of your current hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
                else: print(f"you consumed 35% of your current hp and unleashed your Skill: {self.skill_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            return 1
        else:
            print("Not enough skill points to unleash Skill! please choose a different move: ")
            return 0  
    #Ultimate class: changed text output
    def ultimate(self,opp):
        if self.energy >= 100:
            dmg = round(self.fullhp*80/100)
            heal= round(self.fullhp*20/100)
            self.hp += heal
            opp.hp -= dmg
            self.energy -= 100
            if opp.hp >= 0:
                print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while healing {heal} hp! Your opponent's hp is now: {opp.hp}")
            else: print(f"you unleashed your Ultimate: {self.ultimate_name} and caused {dmg} dmg while healing {heal} hp! Your opponent's hp is now: 0")
            return 1
        else:
            print("Not enough energy to unleash Ultimate! please choose a different move: ")
            return 0
        


class Blade():
    def __init__(self, hp = 4000):
        self.name = "Blade"
        self.skill_name = "Hellscape"
        self.ultimate_name = "Death Sentence"
        self.na_name = "Shard Sword"
        self.na_name_enhanced = "Forest of swords"
        self.hellscape = 0
        self.counter = 0
        self.stack = 0
        self.hp = hp
        self.fullhp = hp
        self.skill_points = 2
        self.energy = 0
        
    def normalAttack(self,opp):
        if self.hp != self.fullhp:
            self.stack += 1
            if self.stack >= 5:
                self.followup(opp)
        if self.hellscape == 0:
            dmg = round(self.fullhp*25/100)
            opp.hp -= dmg
            self.skill_points += 1
            self.energy += 15
            if opp.hp >= 0:
                print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You unleashed your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
        else:
            self.counter += 1
            if self.stack >= 5:
                self.followup(opp)
            dmg = round(self.fullhp*37/100)
            self.hp -= round(self.hp*25/100)
            self.stack += 1
            self.energy += 30
            opp.hp -= dmg
            if opp.hp >= 0:
                print(f"You consumed 25% of your hp to unleash your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: {opp.hp}")
            else: print(f"You consumed 25% of your hp to unleash your Normal Attack: {self.na_name} and caused {dmg} dmg! Your opponent's hp is now: 0")
            if self.counter == 2:
                print("Exited Hellscape mode!")
                self.hellscape = 0
                self.counter = 0
        return 1
    
    def followup(self,opp):
        dmg = round(self.fullhp*60/100)
        heal = round(self.fullhp*25/100)
        self.hp += heal
        opp.hp -= dmg
        print(f"Performed the Follow-up ATK and caused {dmg} while healing {heal}")
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
        if self.energy >= 100:
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