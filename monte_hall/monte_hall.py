import math
import random
import pygal

def monte_hall():
    doors = [0, 1, 2]

    initial_selected_door, winning_door = random.choice(doors), random.choice(doors)
    switch_door, open_door = 0, 0

    switch, no_switch = False, False

    if initial_selected_door == winning_door:
        # the initially chosen door covered the prize, so the player must choose
        # from the remaining two doors at random, but both contain non-prizes
        doors.remove(initial_selected_door)
        open_door = random.choice(doors)

        doors.remove(open_door)
        switch_door = random.choice(doors)

    else:

        # the initially chosen door covered a non-prize, so by switching,
        # the player is garunteed to uncover the prize. By removing the initial 
        # door selection and the winning door, we can find the door that is opened
        # to reveal a non-prize. Then, switching will doors means that player will
        # choose the door covering the prize
        doors.remove(initial_selected_door)
        doors.remove(winning_door)

        open_door = doors[0]

        winning_door = switch_door

    if switch_door == winning_door:
        switch = True
    else:
        switch = False

    return switch

def main():
    iterations = 1000
    switch, no_switch = list(), list()

    switch_count, no_switch_count = 0, 0

    for i in range(iterations):

        i = i+1

        for j in range(i):

            s = monte_hall()

            if s:
                switch_count += 1

        # computing proportion of success attributed to switching and not switching
        no_switch_count = i - switch_count

        assert(no_switch_count + switch_count == i)

        switch.append(switch_count / i)
        no_switch.append(no_switch_count / i)

        # reset the counts before next iteration
        switch_count, no_switch_count = 0, 0

    # plot the line graph via the pygal library
    line_chart = pygal.Line(show_x_labels=False)
    line_chart.title = 'Monte Hall Problem'
    line_chart.x_labels = map(str, range(0, iterations))
    line_chart.add('Switched', switch)
    line_chart.add('Didn\'t Switch', no_switch)
    line_chart.render_to_file('monte_hall.svg')

if __name__ == "__main__":
    main()