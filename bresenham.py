import matplotlib.pyplot as plt

# Function for Bresenham's line generation
def bresenham(x1, y1, x2, y2):
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        points.append((x, y))

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to increment y and update slope error
        if slope_error_new >= 0:
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
    
    return points

# Driver code
if __name__ == '__main__':
    # Take input from user
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))

    # Function call
    points = bresenham(x1, y1, x2, y2)

    # Plotting using matplotlib for visualization
    x_coords, y_coords = zip(*points)
    
    plt.figure(figsize=(4,4))
    plt.plot(x_coords, y_coords, marker="o", markersize=1, markerfacecolor="green")
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Bresenham's Line Generation")
    plt.grid(True)

    # Draw x and y axis lines to divide the plot into quadrants
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Set fixed limits for the plot
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    
    # Ensure the aspect ratio is equal
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()
