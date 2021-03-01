import matplotlib.pyplot as plt
import numpy as np

def change(arr):
    x = []
    y = []
    for i in range(len(arr)):
        x.append(arr[i][0])
        y.append(arr[i][1])
    x = np.array(x)
    y = np.array(y)
    return x, y


plt.ion()  # Turn on interactive mode
plt.subplots()
plt.xlim(-1, 7)
plt.ylim(-1, 7)

arr = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
arr = np.array(arr)
x, y = change(arr)
ax = plt.scatter(x, y)
for j in range(100):
    plt.clf()          # Clear the canvas
    plt.xlim(-1, 7)            # Because the canvas is emptied, the range of the coordinate axis needs to be reset
    plt.ylim(-1, 7)
    for i in range(6):
        arr[i][0] = np.random.randint(0,6,1)
        arr[i][1] = np.random.randint(0,6,1)
    x, y = change(arr)
    plt.scatter(x, y)
    plt.pause(0.2)
plt.ioff()
plt.show()