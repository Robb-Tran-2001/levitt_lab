import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as pyxl

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
figure = plt.figure("Graph 1: No Separating Peripheral Channels")
figure2 = plt.figure("Graph 2: Separating Peripheral Channels by Color")
figure3 = plt.figure("Graph 3: 10-20 Electrodes")
figure4 = plt.figure("Graph 4: 10-10 Electrodes")

#create graph to draw on figure
graph = figure.add_subplot(projection = "3d")
graph2 = figure2.add_subplot(projection = "3d")
graph3 = figure3.add_subplot(projection = "3d")
graph4 = figure4.add_subplot(projection = "3d")

#flags to add label once when drawing scatterplot. set to False immediately after
flag_first_periph = True
flag_first_nperiph = True
flag_first_1020 = True
flag_first_1010 = True
first_non_electrode = True

#for each point in the data set
for i in range(len(data_in_array_form)):
    #grab x, y, z, and channel name
    x = data_in_array_form[i][1]
    y = data_in_array_form[i][2]
    z = data_in_array_form[i][3]
    channel_name = data_in_array_form[i][0]
    graph.scatter(x, y, z, color='b')

    """GRAPHING PERIPHERAL CHANNELS"""
    #if is peripheral channel
    if data_in_array_form[i][4] == 1:
        #if first point, add label
        if flag_first_periph: 
            graph2.scatter(x, y, z, color='y', label="peripheral channel")
            graph3.scatter(x, y, z, color='y', label="peripheral channel")
            graph4.scatter(x, y, z, color='y', label="peripheral channel")
            flag_first_periph = False #set flag to false
        #plot normally without label
        else: 
            graph2.scatter(x, y, z, color='y')
            graph3.scatter(x, y, z, color='y')
            graph4.scatter(x, y, z, color='y')
    
    #if is not peripheral channel
    else: 
        #if first point, add label
        if flag_first_nperiph:
            graph2.scatter(x, y, z, color='b')
            graph3.scatter(x, y, z, color='b')
            graph4.scatter(x, y, z, color='b')
            flag_first_nperiph = False
        #plot normally without label
        else: 
            graph2.scatter(x, y, z, color='b')
            graph3.scatter(x, y, z, color='b')
            graph4.scatter(x, y, z, color='b')

    #add channel numbers onto the graph's corresponding points
    graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    graph2.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    graph3.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    graph4.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')

    """GRAPH 3 AND 4"""
    #do this if it's an electrode point
    if channel_name in electrodes_dict.keys():
        #label as electrode point
        graph3.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size = 6, zorder = 1, color ='k')
        graph4.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size = 6, zorder = 1, color ='k')
        if electrodes_dict[channel_name][1]: #if it is 10_20 electrode, color red in 3 and 4
            if flag_first_1020: 
                graph3.scatter(x, y, z, color = 'r', label="10_20 electrode") 
                graph4.scatter(x, y, z, color = 'r', label="10_20 electrode") 
                flag_first_1020 = False
            else:
                graph3.scatter(x, y, z, color = 'r') 
                graph4.scatter(x, y, z, color = 'r') 
        else: #if it's not, 10_20 electrode, it still is 10_10 electrode, color green in graph 4
            if flag_first_1010: 
                graph4.scatter(x, y, z, color = 'g', label="10_10 electrode") 
                flag_first_1010 = False
            else:
                graph4.scatter(x, y, z, color = 'g') 
    #not an electrode point
    elif not data_in_array_form[i][4]:
        #if first non-electrode point for graph3 and 4
        if first_non_electrode:
            graph3.scatter(x, y, z, color = 'b', label="normal electrode")
            graph4.scatter(x, y, z, color = 'b', label="normal electrode")
            first_non_electrode = False
        else:
            graph3.scatter(x, y, z, color = 'b')
            graph4.scatter(x, y, z, color = 'b')
        graph3.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
        graph4.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')

#set first graph's axis
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')

#set second graph's axis
graph2.set_xlabel('x')
graph2.set_ylabel('y')
graph2.set_zlabel('z')
graph2.legend()

#set second graph's axis
graph3.set_xlabel('x')
graph3.set_ylabel('y')
graph3.set_zlabel('z')
graph3.legend()

#set second graph's axis
graph4.set_xlabel('x')
graph4.set_ylabel('y')
graph4.set_zlabel('z')
graph4.legend()

#display
plt.legend(loc="upper left")
plt.show()