import plotly.plotly as py
from plotly.graph_objs import *
import plotly
import pygal

def main():
    plotly.tools.set_credentials_file(username='jshiohaha', api_key='9OcOUfh0TCX93N5tzPm5')

    probabilities = dict()
    x, y = [], []

    file = open("birthdays.txt", "r")
    for line in file:
        line = line.split(",")
        x.append(line[0]) 
        y.append(float(line[1]) * 100)

    file.close()

    # Start format of scatter plot here
    # trace = Scatter(
    #     x = x,
    #     y = y,
    # )

    # data = [trace]

    # plot_url = py.plot(data, filename="birthday_probabilities")

    # print(plot_url)
    
    line_chart = pygal.Line(show_x_labels=False)
    line_chart.title = 'Birthday Probabilities (in %)'
    line_chart.x_labels = map(str, range(2, 365))
    line_chart.add('', y)
    line_chart.render_to_file('birthday_probabilities.svg')

if __name__ == "__main__":
    main()
