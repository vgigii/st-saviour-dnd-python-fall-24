import time
from tav import Tav
import random
from draw import draw_d20, draw_d4, draw_d6

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)  # Delay for dramatic effect
    print()

# class list containing character roles and their stats
class_list = {
    "Hunter": {"strength": 10, "dexterity": 14, "intelligence": 8},
    "Explorer": {"strength": 8, "dexterity": 12, "intelligence": 12},
    "Warrior": {"strength": 14, "dexterity": 10, "intelligence": 8},
}

# monster choice probabilities
probabilities = [0.5, 0.3333, 0.1667]

# function to generate a monster with different difficulties
def generate_monster():
    monsters = [('Goblin 👺 ', 5), ('Orc 🧌 ', 10), ('Dragon 🐉 ', 15)]
    chosen_index = random.choices(range(len(monsters)), probabilities)[0]  # choose a monster based on probabilities
    monster = monsters[chosen_index]
    # print monster appearance and difficulty
    print_dramatic_text('Oh no! A wild ' + monster[0] + ' has appeared! Difficulty: ' + str(monster[1]))
    print_dramatic_text('Roll above a ' + str(monster[1]) + ' to get rid of the monster!')
    return monster[1]  # return the monster's difficulty

# character class to handle the player's stats, level, and actions
class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.stats = class_list[role]  # set stats based on the chosen class
        self.level = 1  # initial level is 1

    # roll function to handle different buffs (advantage, guidance, or no buff)
    def roll(self, buff):
        if buff == "advantage":  # advantage: roll two d20s and pick the higher result
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 20)
            draw_d20(roll1)
            draw_d20(roll2)
            return max(roll1, roll2)
        elif buff == "guidance":  # guidance: roll d20 and d4, then add both results
            roll1 = random.randint(1, 20)
            roll2 = random.randint(1, 4)
            draw_d20(roll1)
            draw_d4(roll2)
            return roll1 + roll2
        else:  # no buff: just roll a d20
            roll = random.randint(1, 20)
            draw_d20(roll)
            return roll

    # initiative roll: adds dexterity bonus (dexterity // 2) to the d20 roll
    def roll_initiative(self):
        return random.randint(1, 20) + self.stats["dexterity"] // 2

    # level up function to increase stats when the player gains a level
    def level_up(self):
        self.level += 1  # increase the player's level
        stat_increase = random.sample(list(self.stats.keys()), 2)  # randomly select two stats to increase
        for stat in stat_increase:
            self.stats[stat] += 1  # increase the selected stats by 1
        # print level up details
        print_dramatic_text('Level up! You are now level ' + str(self.level) + '.')
        print_dramatic_text('Stats increased: ' + str(stat_increase) + '.') 
        print_dramatic_text('New stats: ' + str(self.stats))

# main game logic
if __name__ == '__main__':
    print('🌲 The Tales of the Wildwood 🌲')

    # collecting user input for the player's name and class
    name = input('Name: ')
    print('Pick a role from the following options:')
    for cls in class_list.keys():
        print('- ' + cls)
    role = ""
    while role not in class_list:  # ensure valid class choice
        role = input('Choose your class: ')
        if role not in class_list:
            print('Invalid class. Choose again.')

    print_dramatic_text('Welcome to Wildwood, ' + name + ' the ' + role + '!')
    player = Character(name, role)  # create player character

    # game logic for handling encounters
    successful_encounters = 0

    # loop to handle monster encounters
    while successful_encounters < 3:
        print("-------------------")
        print("A new challenge awaits!")
        monster_difficulty = generate_monster()  # generate a random monster

        # initiative roll to determine who goes first (player vs. monster)
        print_dramatic_text("Rolling for initiative...")
        player_roll = random.randint(1, 20)  # player rolls a d20
        monster_roll = random.randint(1, 20)  # monster rolls a d20

        # draw the dice rolls
        draw_d20(player_roll)
        draw_d20(monster_roll)

        # calculate initiative with player's dexterity bonus
        player_initiative = player_roll + player.stats["dexterity"] // 2
        # display the initiative calculation and result
        print_dramatic_text('You rolled ' + str(player_roll) + ' + ' + str(player.stats["dexterity"] // 2) + ' (dexterity bonus) = ' + str(player_initiative) + '.')
        print_dramatic_text('The monster rolled ' + str(monster_roll) + '.')

        # determine who goes first based on initiative
        if player_initiative >= monster_roll:
            print_dramatic_text('You go first!')
            player_turn = True
        else:
            print_dramatic_text('The monster attacks first!')
            player_turn = False

        # rolling with buffs (only if it's the player's turn)
        if player_turn:
            buff = input('Enter your buff (advantage/guidance/none): ').lower()  # player chooses a buff
            roll_result = player.roll(buff)  # roll the dice based on chosen buff
            print_dramatic_text('You rolled a ' + str(roll_result) + ' !')

            # check for critical rolls
            if roll_result == 20:
                print_dramatic_text('CRITICAL SUCCESS! The monster is vanquished instantly!')
                successful_encounters += 1  # player defeats the monster
                player.level_up()  # level up the player
                continue
            elif roll_result == 1:
                print_dramatic_text('CRITICAL FAILURE! You stumble and fall. GAME OVER! ☠️')
                break

            # regular success/failure based on the monster's difficulty
            if roll_result >= monster_difficulty:
                print_dramatic_text('YOU HAVE DEFEATED THE MONSTER!')
                successful_encounters += 1  # player defeats the monster
                player.level_up()  # level up the player
            else:
                print_dramatic_text('YOU FAILED, GAME OVER! ☠️')
                break
        else:
            print_dramatic_text('The monster attacks! You were caught off guard and lost the encounter!')
            print_dramatic_text('GAME OVER! ☠️')
            break

        # victory condition: player wins after 3 successful encounters
        if successful_encounters == 3:
            print_dramatic_text('CONGRATULATIONS! You have survived the Wildwood!')