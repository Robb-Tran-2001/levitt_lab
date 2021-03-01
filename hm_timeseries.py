import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

#iteration goes from 4 to 1254, function gets color at iteration
def update(iteration, data, graph):
    #get voltage data to map to color
    voltages_array = []
    for datum in data:
        voltages_array.append(datum[iteration])

    min_v =  min(voltages_array)
    max_v =  max(voltages_array)

    #get color in column iteration, normalize
    norm = colors.Normalize(vmin=min_v, vmax=max_v, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=cm.get_cmap("plasma_r"))
    return (voltages_array, mapper)

#begin here
dataset = pd.read_csv('VoltageTimeSeries_Updated.csv') #read csv into dataframe
data = dataset.to_numpy() #convert dataframe to array
col_name = list(dataset.columns.values.tolist())

figure = plt.figure("Graph")
graph = figure.add_subplot(projection = "3d")

for iteration in range(4, 254):
    voltages_array, mapper = update(iteration, data, graph)
    for i in range(len(data)):
        name = data[i][0]
        x = data[i][1]
        y = data[i][2]
        z = data[i][3]
        voltage = voltages_array[i]
        graph.scatter(x, y, z, color=cm.get_cmap("plasma_r")(mapper.to_rgba(voltage)[0]), marker='o')
        graph.text(x, y, z, '%s' %(name), size=6, zorder=1, color='k')
    plt.title("Heatmap at time " + str(col_name[iteration]))
    plt.pause(0.5)
    graph.clear()

cb = figure.colorbar(mapper)
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
    