import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as pyxl

workbook = pyxl.load_workbook('10-10 and 10-20 electrodes.xlsx') #read csv into dataframe

worksheet = workbook.active
data = list(worksheet.iter_rows(values_only=True))

figure_1010 = plt.figure("Graph 3")
figure_1020 = plt.figure("Graph 4")

graph_3 = figure_1010.add_subplot(projection = "3d")
graph_4 = figure_1020.add_subplot(projection = "3d")

for item in data:
    print(item, "\n")
    
# #flags to add label once when drawing scatterplot
# flag_first_periph = True
# flag_first_nperiph = True

# #for each point in the data set
# for i in range(len(data_in_array_form)):
#     #grab x, y, z, and channel name
#     x = data_in_array_form[i][1]
#     y = data_in_array_form[i][2]
#     z = data_in_array_form[i][3]
#     channel_name = data_in_array_form[i][0]
#     graph.scatter(x, y, z, color='b')

#     #if is peripheral channel
#     if data_in_array_form[i][4] == 1:
#         #if first point, add label
#         if flag_first_periph: 
#             graph_colored.scatter(x, y, z, color='r', label="is peripheral channel")
#             flag_first_periph = False #set flag to false
#         #plot normally without label
#         else: graph_colored.scatter(x, y, z, color='r')
#     #if is not peripheral channel
#     else: 
#         #if first point, add label
#         if flag_first_nperiph:
#             graph_colored.scatter(x, y, z, color='b', label="is NOT peripheral channel")
#             flag_first_nperiph = False
#         #plot normally without label
#         else: graph_colored.scatter(x, y, z, color='b')
#     #add channel numbers onto the graph's corresponding points
#     graph.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')
#     graph_colored.text(x, y, z, '%s' %(channel_name), size=6, zorder=1, color='k')

# #set first graph's axis
# graph.set_xlabel('x')
# graph.set_ylabel('y')
# graph.set_zlabel('z')

# #set second graph's axis and legends
# graph_colored.set_xlabel('x')
# graph_colored.set_ylabel('y')
# graph_colored.set_zlabel('z')
# plt.legend(loc="upper left")

# #display
# plt.show()