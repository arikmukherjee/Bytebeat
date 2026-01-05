import matplotlib.pyplot as plt

def draw_axis(ax):
    ax.plot([-200, 200], [0, 0], 'k-', linewidth=0.5)
    ax.plot([0, 0], [-200, 200], 'k-', linewidth=0.5)
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)

def draw_window(ax, _from, _to):
    ax.plot([_from[0], _to[0], _to[0], _from[0], _from[0]], 
            [_from[1], _from[1], _to[1], _to[1], _from[1]], 'b-')

def draw_object(ax, coor):
    ax.plot(coor[0], coor[1], 'ro', markersize=5)

def algorithm(window_from, window_to, coor):
    xw_min, yw_min = window_from[0]
    xw_max, yw_max = window_from[1]
    xv_min, yv_min = window_to[0]
    xv_max, yv_max = window_to[1]
    xw, yw = coor

    xv = xv_min + ((xw - xw_min) * ((xv_max - xv_min) / (xw_max - xw_min)))
    yv = yv_min + ((yw - yw_min) * ((yv_max - yv_min) / (yw_max - yw_min)))

    return xv, yv

if __name__ == "__main__":
    # Input windows and object coordinates
    print("Enter coordinates for window 1 (from):")
    window1_from = list(map(int, input("From: ").strip().split()))
    window1_to = list(map(int, input("To: ").strip().split()))
    
    print("Enter coordinates for window 2 (to):")
    window2_from = list(map(int, input("From: ").strip().split()))
    window2_to = list(map(int, input("To: ").strip().split()))
    
    object_coor = list(map(int, input("Object: ").strip().split()))

    # Initialize matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    draw_axis(ax)

    # Draw window 1 and window 2
    draw_window(ax, window1_from, window1_to)
    draw_window(ax, window2_from, window2_to)

    # Perform coordinate transformation
    x, y = algorithm([window1_from, window1_to], [window2_from, window2_to], object_coor)

    # Draw object after transformation
    draw_object(ax, [x, y])

    ax.set_title('After Transformation')
    ax.set_aspect('equal')
    plt.grid(True)
    plt.show()
