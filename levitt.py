import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
figure = plt.figure("Graph")

#create graph to draw on figure
graph = figure.add_subplot(projection = "3d")

#flags to add label once when drawing scatterplot. set to False immediately after
flag_first_periph = True
flag_first_nperiph = True
flag_first_1020 = True
flag_first_1010 = True
first_normal = True

flag = 0
while flag not in {1, 2, 3, 4}:
    flag = int(input("Enter a number from 1 to 4. 1 Highlights all electrodes as grey, 2 colors peripheral channels red, 3 makes 10-20 green, 4 makes 10-10 blue: "))

#for each point in the data set

for i in range(len(data_in_array_form)):
    #grab x, y, z, and channel name
    x = data_in_array_form[i][1]
    y = data_in_array_form[i][2]
    z = data_in_array_form[i][3]
    channel_name = data_in_array_form[i][0]
    
    if flag == 1:
        graph.scatter(x, y, z, color='grey')
        graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    elif flag == 2:
        if data_in_array_form[i][4]:
            graph.scatter(x, y, z, color='red')
        else:
            graph.scatter(x, y, z, color='grey')
        graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    elif flag == 3:
        if channel_name in electrodes_dict.keys() and electrodes_dict[channel_name][1] == 1:
            graph.scatter(x, y, z, color='green')
            graph.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size=6, zorder=1, color='k')
        else: 
            graph.scatter(x, y, z, color='grey')
            graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
    elif flag == 4:
        if channel_name in electrodes_dict.keys() and electrodes_dict[channel_name][2] == 1:
            graph.scatter(x, y, z, color='blue')
            graph.text(x, y, z, '%s' %(electrodes_dict[channel_name][0]), size=6, zorder=1, color='k')
        else:
            graph.scatter(x, y, z, color='grey')
            graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')


#set first graph's axis
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
grey_patch = mpatches.Patch(color='grey', label='Normmal')
red_patch = mpatches.Patch(color='red', label='Peripheral')
green_patch = mpatches.Patch(color='green', label='10-20')
blue_patch = mpatches.Patch(color='blue', label='10-10')

legends=[grey_patch]
if flag==2: legends.append(red_patch)
elif flag==3: legends.append(green_patch)
elif flag==4: legends.append(blue_patch)

plt.legend(handles=legends, loc = "upper left")
plt.show()