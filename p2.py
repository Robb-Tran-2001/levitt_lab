import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as pyxl
import matplotlib.patches as mpatches

workbook = pyxl.load_workbook('10-10 and 10-20 electrodes.xlsx') #read csv into dataframe
worksheet = workbook.active
electrodes = list(worksheet.iter_rows(values_only=True))
electrodes_dict = {}
for item in electrodes:
    value = (item[1], item[2], item[3])
    electrodes_dict[item[0]] = value

data = pd.read_csv('129Channels.csv') #read csv into dataframe

data_in_array_form = data.to_numpy() #convert dataframe to array
 
#create figures to render out to 
figure = plt.figure("Graph 1: 10-20 Electrodes")
figure2 = plt.figure("Graph 2: 10-10 Electrodes")

#create graph to draw on figure
graph = figure.add_subplot(projection = "3d")
graph2 = figure2.add_subplot(projection = "3d")

#for each point in the data set
for i in range(len(data_in_array_form)):
    #grab x, y, z, and channel name
    x = data_in_array_form[i][1]
    y = data_in_array_form[i][2]
    z = data_in_array_form[i][3]
    channel_name = data_in_array_form[i][0]
    if channel_name in electrodes_dict.keys():
        if electrodes_dict[channel_name][1]: #10-20
            graph.scatter(x, y, z, color='green')
            graph.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size=6, zorder=1, color='k')
        else:
            graph.scatter(x, y, z, color='grey')
            graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
        if electrodes_dict[channel_name][2]: #10-20
            graph2.scatter(x, y, z, color='blue')
            graph2.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size=6, zorder=1, color='k')
    else:
        if data_in_array_form[i][4]: #peripheral
            graph.scatter(x, y, z, color='red')
            graph2.scatter(x, y, z, color='red')
        else: 
            graph.scatter(x, y, z, color='grey')
            graph2.scatter(x, y, z, color='grey')
        graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
        graph2.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')

grey_patch = mpatches.Patch(color='grey', label='Normmal')
red_patch = mpatches.Patch(color='red', label='Peripheral')
green_patch = mpatches.Patch(color='green', label='10-20')
blue_patch = mpatches.Patch(color='blue', label='10-10')

legends1 = [grey_patch, red_patch, green_patch]
legends2 = [grey_patch, red_patch, blue_patch]

#set second graph's axis
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
graph.legend(handles=legends1, loc="upper left")

#set second graph's axis
graph2.set_xlabel('x')
graph2.set_ylabel('y')
graph2.set_zlabel('z')
graph2.legend(handles=legends2, loc="upper left")

#hello there
plt.show()