import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('129Channels.csv') #read csv into dataframe

data_in_array_form = data.to_numpy() #convert dataframe to array
 
#create figures to render out to 
figure = plt.figure("Graph 1: No Separating Peripheral Channels")
figure_colored = plt.figure("Graph 2: Separating Peripheral Channels by Color")

#create graph to draw on figure
graph = figure.add_subplot(projection = "3d")
graph_colored = figure_colored.add_subplot(projection = "3d")

#flags to add label once when drawing scatterplot
flag_first_periph = True
flag_first_nperiph = True

#for each point in the data set
for i in range(len(data_in_array_form)):
    #grab x, y, z, and channel name
    x = data_in_array_form[i][1]
    y = data_in_array_form[i][2]
    z = data_in_array_form[i][3]
    channel_name = data_in_array_form[i][0]
    graph.scatter(x, y, z, color='b')

    #if is peripheral channel
    if data_in_array_form[i][4] == 1:
        #if first point, add label
        if flag_first_periph: 
            graph_colored.scatter(x, y, z, color='r', label="is peripheral channel")
            flag_first_periph = False #set flag to false
        #plot normally without label
        else: graph_colored.scatter(x, y, z, color='r')
    #if is not peripheral channel
    else: 
        #if first point, add label
        if flag_first_nperiph:
            graph_colored.scatter(x, y, z, color='b', label="is NOT peripheral channel")
            flag_first_nperiph = False
        #plot normally without label
        else: graph_colored.scatter(x, y, z, color='b')
    #add channel numbers onto the graph's corresponding points
    graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    graph_colored.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')

#set first graph's axis
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')

#set second graph's axis and legends
graph_colored.set_xlabel('x')
graph_colored.set_ylabel('y')
graph_colored.set_zlabel('z')
plt.legend(loc="upper left")

#display
plt.show()