import random

class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

        self.level = 1
        self.strength = 0
        self.wisdom = 0
        self.charisma = 0
        self.intelligence = 0
        self.constitution = 0
        self.dexterity = 0 


        self.assign_stats()
        
    def print_character_sheet_(self):
        print('Name: ' + self.name)
        print('Role: ' + self.role)
        print('Level: ' + str(self.level))
        print('-------------------')
        print('-- Player Stats --')
        print('Strength: ' + str(self.strength))    
        print('Wisdom: ' + str(self.wisdom))
        print('Charisma: ' + str(self.charisma))
        print('Intelligence: ' + str(self.intelligence))
        print('Constitution:' + str(self.constitution))
        print('Dexterity: ' + str(self.dexterity))

    def assign_stats(self):
        stats = [15,14,13,12,10,8]
        random.shuffle(stats)
        self.strength = stats[0]
        self.wisdom = stats[1]
        self.charisma = stats[2]
        self.intelligence = stats[3]
        self.constitution = stats[4]
        self.dexterity = stats[5]

    def roll(self, buff=None):
        if buff == "advantage":
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            print('Rolling with advantage: ' + roll1 , roll2)
            return max(roll1, roll2)
        elif buff == "guidance":
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 4)
            print('Rolling with guidance: ' + roll1 , roll2 )
            return (roll1 + roll2)
        else:
            roll = random.randint(1, 20)
            print('Rolling without buffs: ' + roll)
            return roll
        
