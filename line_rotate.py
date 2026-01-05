import matplotlib.pyplot as plt
import numpy as np

# Function for Bresenham's line generation
def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return points

# Function to rotate a point around a pivot
def rotate_point(x, y, angle, pivot):
    angle_rad = np.radians(angle)
    ox, oy = pivot
    px, py = x - ox, y - oy
    qx = ox + np.cos(angle_rad) * px - np.sin(angle_rad) * py
    qy = oy + np.sin(angle_rad) * px + np.cos(angle_rad) * py
    return qx, qy

# Function to rotate a list of points around a pivot
def rotate_points(points, angle, pivot):
    return [rotate_point(x, y, angle, pivot) for x, y in points]

# Driver code
if __name__ == '__main__':
    # Take input from user
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))
    angle = float(input("Enter the rotation angle in degrees: "))

    # Generate the line points
    points = bresenham(x1, y1, x2, y2)
    
    # Rotate the line points
    pivot = (x1, y1)  # Rotate around the first point
    rotated_points = rotate_points(points, angle, pivot)
    
    # Extract x and y coordinates for original and rotated points
    x_coords, y_coords = zip(*points)
    rotated_x_coords, rotated_y_coords = zip(*rotated_points)
    
    # Plot the original and rotated lines
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, marker="o", markersize=2, markerfacecolor="green", label="Original Line")
    plt.plot(rotated_x_coords, rotated_y_coords, marker="o", markersize=2, markerfacecolor="red", label="Rotated Line")
    
    # Draw x and y axis lines to divide the plot into quadrants
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Bresenham's Line Rotation")
    plt.grid(True)
    plt.legend()

    # Set fixed limits for the plot
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    
    # Ensure the aspect ratio is equal
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()
