#####################
# import modules
#####################

import random
import math

#####################
# Define class
#####################


class Warrior:
    def __init__(self, name="warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        random_attk = random.random()
        attk_amt = self.attk_max * (random_attk + .5)
        return attk_amt

    def block(self):
        # Randomly calculate how much of the attack was blocked
        random_block = random.random()
        block_amt = self.block_max * (random_block + .5)
        return block_amt


class Battle:
    def start_fight(self, warrior1, warrior2):
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def get_attack_result(warriorA, warriorB):
        warrior_a_attk_amt = warriorA.attack()
        warrior_b_block_amt = warriorB.block()
        damage_2_warrior_b = math.ceil(warrior_a_attk_amt - warrior_b_block_amt)
        warriorB.health = warriorB.health - damage_2_warrior_b

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage_2_warrior_b))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    thor = Warrior("Thor", 50, 20, 10)
    loki = Warrior("Loki", 50, 20, 10)
    # Create Battle object
    battle = Battle()
    # Initiate Battle
    battle.start_fight(thor, loki)



