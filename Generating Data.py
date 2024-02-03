# Data visualization involves exploring data through visual representations. It's closely associated with data mining, which uses code to explore patterns and connections in a data set. 
# A data set can be just a small list of numbers, that fits in one line of code or many gigabites of data.  

# Visualizing data is much more about generating pretty pictures, bar graphs, or pie chart, it is about finding the relations and patterns in the data that is given. 
# Thus in order to visualize data, you don't need a super computer, with python's efficiency, you can visualize complex data with just a laptop, with all the python's array of 
# visualization and analysis tools available in the python library. 

"""We'll be using the matplotlib module from the python library, which is the mathematical plotting library, which is used to create beautiful and meaningful patterns from data sets. 
From what I understand is that data visualization is all about providing a clear representation of the cluttered data that is there and turning it into a meaningful picture.
- We'll be using the matplotlib module from the python's library, but first we need to install matplotlib on our computer. """                                

import matplotlib.pyplot as plt
# Here we import the pyplot module using the alias plt so that we don't have to type pyplot repeatedly. You'll see the plt convention a lot in online examples, thus we'll follow the same. 
 
squares = [1,4,9,16,25] # We create a list to hold the squares and then pass it to the plot() function, which will try and plot the numbers in a meaningful way.
plt.plot(squares)
plt.show() # The plt.show() method will open matplotlib's viewer and displays the plot. You can zoom the plotted graph or save it as a picture in png format.




