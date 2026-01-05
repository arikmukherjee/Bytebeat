def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    
    # List to store the points
    points = []
    
    # Initial point on the axes after translation
    points.append((x + x_centre, y + y_centre))
    print(f"({x + x_centre}, {y + y_centre})", end=" ")

    # When radius is zero only a single point is printed
    if r > 0:
        points.append((x + x_centre, -y + y_centre))
        points.append((y + x_centre, x + y_centre))
        points.append((-y + x_centre, x + y_centre))
        print(f"({x + x_centre}, {-y + y_centre})", end=" ")
        print(f"({y + x_centre}, {x + y_centre})", end=" ")
        print(f"({-y + x_centre}, {x + y_centre})", end=" ")

    # Initial value of P
    P = 1 - r

    while x > y:
        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1
        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have already been printed
        if x < y:
            break

        # Printing the generated points and their reflections
        points.append((x + x_centre, y + y_centre))
        points.append((-x + x_centre, y + y_centre))
        points.append((x + x_centre, -y + y_centre))
        points.append((-x + x_centre, -y + y_centre))
        print(f"({x + x_centre}, {y + y_centre})", end=" ")
        print(f"({-x + x_centre}, {y + y_centre})", end=" ")
        print(f"({x + x_centre}, {-y + y_centre})", end=" ")
        print(f"({-x + x_centre}, {-y + y_centre})", end=" ")

        if x != y:
            points.append((y + x_centre, x + y_centre))
            points.append((-y + x_centre, x + y_centre))
            points.append((y + x_centre, -x + y_centre))
            points.append((-y + x_centre, -x + y_centre))
            print(f"({y + x_centre}, {x + y_centre})", end=" ")
            print(f"({-y + x_centre}, {x + y_centre})", end=" ")
            print(f"({y + x_centre}, {-x + y_centre})", end=" ")
            print(f"({-y + x_centre}, {-x + y_centre})", end=" ")
    
    print()
    return points

# Driver Code
if __name__ == '__main__':
    # Take input from user
    x_centre = int(input("Enter the x-coordinate of the center: "))
    y_centre = int(input("Enter the y-coordinate of the center: "))
    r = int(input("Enter the radius of the circle: "))

    # Function call
    points = midPointCircleDraw(x_centre, y_centre, r)

    # Optionally plot the points using matplotlib for visualization
    import matplotlib.pyplot as plt
    
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, marker="o", color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Mid-point Circle Drawing Algorithm")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
