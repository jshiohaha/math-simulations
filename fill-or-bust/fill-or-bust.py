import sys
import random
import pygal

import scipy as sp
import numpy as np
from scipy import stats

WINNING_DIGIT = [1,5]
NUM_TRIALS = 10000

def main():
    outcomes = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
    rolls = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }

    for _ in range(NUM_TRIALS):
        num_die = 6
        roll = 1
        while num_die > 0:
            num_dice_before_roll = num_die
            for _ in range(num_die):
                die = random.randint(1,6)
                rolls[die] += 1

                if die not in WINNING_DIGIT:
                    num_die -= 1
            roll += 1

        outcomes[num_dice_before_roll] += 1

    plot_distributions(rolls)
    plot_outcomes(outcomes)
    continue_roll_probabilities()


def continue_roll_probabilities():
    for i in range(1,7):
        prob_of_continuing = 1-stats.binom.cdf(0, i, (1/3))
        print("Probabilities of continuing to roll with " + str(i) + " dice: " + str(prob_of_continuing))


def plot_outcomes(outcomes):
    outcome_percentages = [round((x/NUM_TRIALS), 4) for x in outcomes.values()]
    line_chart = pygal.Line()
    line_chart.title = 'Number of Dice on Losing Roll on ' + str(NUM_TRIALS) + ' rolls.'
    line_chart.x_labels = map(str, range(1, 7))
    line_chart.add('', outcome_percentages)
    line_chart.render_to_file('fill-or-bust.svg')


def plot_distributions(rolls):
    a = np.array([int(x) for x in rolls.values()])
    mean = np.mean(a)
    var = np.var(a)

    line_chart = pygal.Bar()
    line_chart.title = 'Dice Roll Distribution on ' + str(NUM_TRIALS) + ' trials.'
    line_chart.x_labels = map(str, range(1, 7))
    line_chart.add('', rolls.values())
    line_chart.render_to_file('roll-distribution-fill-or-bust.svg')

if __name__ == "__main__":
    main()