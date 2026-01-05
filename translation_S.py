import matplotlib.pyplot as plt
import numpy as np

def translation(coor, translation_vector):
    coor = np.array(coor)  # Convert coordinates to numpy array
    translation_matrix = np.array([
        [1, 0, translation_vector[0]],
        [0, 1, translation_vector[1]],
        [0, 0, 1]
    ])
    translated = np.dot(translation_matrix, np.vstack((coor.T, np.ones(len(coor)))))[:2].T
    return translated.tolist()

def draw_xy_axes():
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)

def draw_polygon(coordinates, color):
    coordinates.append(coordinates[0])  # Closing the polygon
    xs, ys = zip(*coordinates)
    plt.fill(xs, ys, color=color, alpha=0.5)

if __name__ == "__main__":
    # Input coordinates
    ipcoor = []
    for i in range(3):
        x, y = map(int, input(f"Coordinate {i+1}: ").strip().split())
        ipcoor.append([x, y])

    # Input translation vector
    tx, ty = map(int, input("(tx, ty): ").strip().split())
    translation_vector = [tx, ty]

    # Perform translation
    opcoor = translation(ipcoor, translation_vector)

    # Plotting
    plt.figure(figsize=(6, 6))
    draw_xy_axes()

    # Plot initial polygon
    draw_polygon(ipcoor, 'gray')
    plt.title('Before Translation')

    # Plot translated polygon
    translated_color = 'blue'  # Color for translated polygon
    draw_polygon(opcoor, translated_color)
    plt.title('After Translation')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()
