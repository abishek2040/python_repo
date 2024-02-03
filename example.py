# Import the matplotlib package 

import matplotlib.pyplot as plt

data = [1,3,5,7,9,11,13,15,30,40,50,100,200]
input_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
plt.plot(input_values, data, linewidth=7)
plt.title("A simple example table.")
plt.xlabel("Values")
plt.ylabel("Numbers")
plt.tick_params(axis="both", labelsize=10)
plt.show()