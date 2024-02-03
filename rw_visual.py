import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    #Set the size of the figure.
    plt.figure(figsize=(10,7))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolors="none")

    # Emphasize the end points: 
    plt.plot(0,0 ,c="green", edgecolors="none")
    plt.plot(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none")

    # Removing the axes to tidy up the figure: 
    plt.axis("off") # Remove both the axis from the figure. 
    plt.show()

    keep_running = input("Would you like to stop? (y/n): \n")
    if keep_running == "y":
        print("Thank you for playing!")
        break
    