from matplotlib import pyplot as plt

# DDA Function for line generation
def DDA(x0, y0, x1, y1):
    # find absolute differences
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # find maximum difference
    steps = max(dx, dy)

    # calculate the increment in x and y
    xinc = dx / steps
    yinc = dy / steps

    # start with 1st point
    x = float(x0)
    y = float(y0)

    # make a list for coordinates
    x_coordinates = []
    y_coordinates = []

    for _ in range(int(steps) + 1):  # including the end point
        # append the x,y coordinates in respective list
        x_coordinates.append(x)
        y_coordinates.append(y)

        # increment the values
        x += xinc if x0 < x1 else -xinc
        y += yinc if y0 < y1 else -yinc

    # plot the line with coordinates list
    plt.plot(x_coordinates, y_coordinates, marker="o", markersize=2, markerfacecolor="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("DDA Line Generation")
    plt.grid(True)
    plt.show()

# Driver code
if __name__ == "__main__":
    # Take input from user
    x0 = int(input("Enter the x-coordinate of the first point: "))
    y0 = int(input("Enter the y-coordinate of the first point: "))
    x1 = int(input("Enter the x-coordinate of the second point: "))
    y1 = int(input("Enter the y-coordinate of the second point: "))

    # Function call
    DDA(x0, y0, x1, y1)
