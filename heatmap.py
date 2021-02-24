import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

dataset = pd.read_csv('129Channels_with_coresponding_voltage_potentials.csv') #read csv into dataframe

data = dataset.to_numpy() #convert dataframe to array

figure = plt.figure("Graph")

graph = figure.add_subplot(projection = "3d")

#get voltage data to map to color
voltages_array = []
for datum in data:
    voltages_array.append(datum[4])

min_v =  min(voltages_array)
max_v =  max(voltages_array)

norm = colors.Normalize(vmin=min_v, vmax=max_v, clip=True)
mapper = cm.ScalarMappable(norm=norm, cmap=cm.get_cmap("plasma_r"))

#get scatterplot
for i in range(len(data)):
    name = data[i][0]
    x = data[i][1]
    y = data[i][2]
    z = data[i][3]
    voltage = voltages_array[i]
    graph.scatter(x, y, z, color=cm.get_cmap("plasma_r")(mapper.to_rgba(voltage)[0]), marker='o')
    graph.text(x, y, z, '%s' %(name), size=6, zorder=1, color='k')

cb = figure.colorbar(mapper)
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
plt.show()
    