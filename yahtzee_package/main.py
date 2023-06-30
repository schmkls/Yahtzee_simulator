import timeit
from yahtzee_package.yahtzee_simulator import YahtzeeSimulator


def main():
    '''
    Prompts for Yahtzee game parameters, runs, and times simulation.
    '''
    print("Enter number of dice in the Yahtzee game: ")
    number_of_dice = int(input())

    print("Enter number of sides on each die: ")
    die_sides = int(input())

    simulator = YahtzeeSimulator(number_of_dice, die_sides)
    execution_time = timeit.timeit(simulator.simulate, number=1)
    print(f'Execution time: {execution_time} seconds')

if __name__ == "__main__":
    main()