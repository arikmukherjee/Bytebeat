import matplotlib.pyplot as plt
import numpy as np

def scaling(coor, scaling_vector):
    coor = np.array(coor)  # Convert coordinates to numpy array
    scaling_matrix = np.array([
        [scaling_vector[0], 0],
        [0, scaling_vector[1]]
    ])
    scaled = np.dot(coor, scaling_matrix)  # Apply scaling matrix directly
    return scaled.tolist()

def draw_xy_axes(ax):
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-200, 200)  # Set xlim to -200 to 200
    ax.set_ylim(-200, 200)  # Set ylim to -200 to 200

def draw_polygon(ax, coordinates, color):
    coordinates.append(coordinates[0])  # Closing the polygon
    xs, ys = zip(*coordinates)
    ax.fill(xs, ys, color=color, alpha=0.5)

if __name__ == "__main__":
    # Input coordinates
    ipcoor = []
    for i in range(3):
        x, y = map(int, input(f"Coordinate {i+1}: ").strip().split())
        ipcoor.append([x, y])

    # Input scaling vector
    Sx, Sy = map(float, input("(Sx, Sy): ").strip().split())
    scaling_vector = [Sx, Sy]

    # Perform scaling
    opcoor = scaling(ipcoor, scaling_vector)

    # Plotting
    fig, ax = plt.subplots(figsize=(6, 6))
    draw_xy_axes(ax)

    # Plot initial polygon
    draw_polygon(ax, ipcoor, 'gray')
    ax.set_title('Before Scaling')

    # Plot scaled polygon
    scaled_color = 'blue'  # Color for scaled polygon
    draw_polygon(ax, opcoor, scaled_color)
    ax.set_title('After Scaling')

    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    plt.show()
