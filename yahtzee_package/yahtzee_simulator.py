import random


class YahtzeeSimulator:
    def __init__(self, number_of_dice: int, die_sides: int):
        '''
        Constructor for the YahtzeeSimulator class.

        param: number of dice: how many dice are in the game
        param: die_sides: the number of sides on each die
        '''
        self.number_of_dice = number_of_dice
        self.die_sides = die_sides

    def simulate(self):
        '''
            Simulates thousand rounds of Yahtzee and prints the maximum score
            for each round.
        '''
        for round in range(1000):
            roll = self.roll_dice()
            sides = set(roll)
            max_score = max(roll.count(side) * side for side in sides)
            print(f'Score: \t{max_score}')

    def roll_dice(self):
        '''Returns a list of random integers representing the dice roll.'''
        roll = []
        for die in range(self.number_of_dice):
            roll.append(random.randint(1, self.die_sides))
        return roll