import matplotlib.pyplot as plt

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    INSIDE = 0  # 0000
    LEFT = 1    # 0001
    RIGHT = 2   # 0010
    BOTTOM = 4  # 0100
    TOP = 8     # 1000

    def compute_code(x, y):
        code = INSIDE
        if x < xmin:
            code |= LEFT
        elif x > xmax:
            code |= RIGHT
        if y < ymin:
            code |= BOTTOM
        elif y > ymax:
            code |= TOP
        return code

    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            outside_code = code1 if code1 != 0 else code2

            if outside_code & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outside_code & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outside_code & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outside_code & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outside_code == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return int(x1), int(y1), int(x2), int(y2)
    else:
        return None

# Get user input for the clipping window coordinates
xmin = float(input("Enter xmin for clipping window: "))
ymin = float(input("Enter ymin for clipping window: "))
xmax = float(input("Enter xmax for clipping window: "))
ymax = float(input("Enter ymax for clipping window: "))

# Get user input for the line segment endpoints
x1 = float(input("Enter x-coordinate of first point of line: "))
y1 = float(input("Enter y-coordinate of first point of line: "))
x2 = float(input("Enter x-coordinate of second point of line: "))
y2 = float(input("Enter y-coordinate of second point of line: "))

# Perform the clipping
clipped = cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'b-')  # Clipping window
plt.plot([x1, x2], [y1, y2], 'g-', label='Original Line')  # Original line

if clipped:
    x1_clip, y1_clip, x2_clip, y2_clip = clipped
    plt.plot([x1_clip, x2_clip], [y1_clip, y2_clip], 'r-', label='Clipped Line')  # Clipped line

plt.xlim(min(xmin, x1, x2) - 50, max(xmax, x1, x2) + 50)
plt.ylim(min(ymin, y1, y2) - 50, max(ymax, y1, y2) + 50)
plt.legend()
plt.title('Cohen-Sutherland Line Clipping')
plt.grid(True)
plt.show()
