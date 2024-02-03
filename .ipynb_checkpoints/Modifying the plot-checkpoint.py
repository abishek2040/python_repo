import matplotlib.pyplot as plt
# Changing the label type and graph thickness. Although the plot from the above plot shows that the numbers are increasing, the label type is too small and the line is too thin. 
# Fortunately, matplotlib allows you to adjust every feature of a visualization. Let's use few of the available customizations to improve the readability of the plot, as shown here: 

# Here we define another data set, list of odd numbers from 1 to 11.

odd = [1,3,5,7,9,11]
plt.plot(odd, linewidth=5) # Changing the line width of the plot.

# Set chart title and label axes.
plt.title("Odd Numbers", fontsize=23)
plt.xlabel("Value", fontsize=23)
plt.ylabel("Odd numbers", fontsize = 15)

# Set the size of tick labels. 
plt.tick_params(axis="both", labelsize=9.5)
plt.show()

    