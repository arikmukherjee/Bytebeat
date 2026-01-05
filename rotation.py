import numpy as np
import matplotlib.pyplot as plt
import math

# Function to rotate coordinates
def rotation(coor, theta):
    theta = np.radians(theta)  # Convert angle to radians
    ipcoor = np.vstack((np.array(coor).transpose(), np.array([1, 1, 1])))
    rotation_matrix = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.dot(rotation_matrix, ipcoor)

# Function to draw XY coordinates
def drawxycoor(ax):
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

# Driving code
if __name__ == "__main__":
    ipcoor = [list(map(int, input(f"Coordinate {i + 1}: ").strip().split())) for i in range(3)]
    rotation_angle = int(input("angle: ").strip())
    opcoor = rotation(ipcoor, rotation_angle)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw X Y coordinates
    drawxycoor(ax)

    # Plot initial object before transformation
    ipcoor = np.array(ipcoor)
    ax.fill(ipcoor[:, 0], ipcoor[:, 1], color='gray', alpha=0.5, label='Before Rotation')

    # Plot final object after transformation
    opcoor = opcoor[:-1]  # Remove the homogeneous coordinate row
    ax.fill(opcoor[0, :], opcoor[1, :], color='blue', alpha=0.5, label='After Rotation')

    # Set fixed limits for the plot
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)

    # Ensure the aspect ratio is equal
    ax.set_aspect('equal', adjustable='box')

    ax.legend()
    plt.title("Rotation Transformation")
    plt.grid(True)
    plt.show()
