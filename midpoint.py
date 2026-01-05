# midPoint function for line generation
def midPoint(X1, Y1, X2, Y2):
    # calculate dx & dy
    dx = X2 - X1
    dy = Y2 - Y1

    # initial value of decision parameter d
    d = dy - (dx / 2)
    x = X1
    y = Y1

    # List to store the points
    points = []
    
    # Plot initial given point
    points.append((x, y))
    print(x, ",", y)

    # iterate through value of X
    while x < X2:
        x += 1

        # E or East is chosen
        if d < 0:
            d = d + dy

        # NE or North East is chosen
        else:
            d = d + (dy - dx)
            y += 1

        # Plot intermediate points
        points.append((x, y))
        print(x, ",", y)
    
    return points

# Driver program
if __name__ == '__main__':
    # Take input from user
    X1 = int(input("Enter the x-coordinate of the first point: "))
    Y1 = int(input("Enter the y-coordinate of the first point: "))
    X2 = int(input("Enter the x-coordinate of the second point: "))
    Y2 = int(input("Enter the y-coordinate of the second point: "))

    # Function call
    points = midPoint(X1, Y1, X2, Y2)

    # Optionally plot the points using matplotlib for visualization
    import matplotlib.pyplot as plt
    
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, marker="o", markersize=2, markerfacecolor="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Mid-point Line Generation")
    plt.grid(True)
    plt.show()
