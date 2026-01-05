import turtle

# Function to draw letter 'A'
def draw_A(t):
    t.speed(1)
    t.penup()
    t.goto(-50, 0)  # Start from the left
    t.pendown()
    t.left(75)
    t.forward(100)  # Diagonal line
    t.right(150)
    t.forward(100)  # Diagonal line
    t.backward(50)   # Halfway back
    t.right(105)
    t.forward(28)   # Top horizontal line

# Function to draw letter 'B'
def draw_B(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.left(90)
    t.forward(140)
    t.right(90)
    t.circle(-35,180)  # Upper arc
    t.circle(35,-180)  # Lower arc
    

# Function to draw letter 'C'
def draw_C(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.circle(50, -180)

# Define other letter drawing functions similarly
def draw_D(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-50,180)

def draw_E(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(50,50)
    t.pendown()
    t.forward(30)
    t.penup()
    t.goto(50,0)
    t.pendown()
    t.forward(50)

def draw_F(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(50,50)
    t.pendown()
    t.forward(30)

def draw_G(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.circle(-50,-180)
    t.circle(-50,-35)
    t.right(125)
    t.forward(30)
    t.left(90)
    t.forward(30)

def draw_H(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.forward(50)

def draw_I(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(100)

def draw_J(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(80)
    t.circle(-35,180)

def draw_K(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.goto(0,0)
    t.left(50)
    t.forward(60)
    t.goto(0,0)
    t.left(90)
    t.forward(60)

def draw_L(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(60)

def draw_M(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(145)
    t.forward(70)
    t.left(110)
    t.forward(70)
    t.right(145)
    t.forward(100)

def draw_N(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(145)
    t.forward(120)
    t.left(145)
    t.forward(100)

def draw_O(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(50)

def draw_P(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,-10)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-30,180)

def draw_Q(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,10)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(15,40)
    t.pendown()
    t.right(35)
    t.fd(50)

def draw_R(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,-10)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-29,180)
    t.left(135)
    t.fd(50)

def draw_S(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(0,60)
    t.pendown()
    t.left(135)
    t.fd(5)
    t.circle(45,200)
    t.right(10)
    t.fd(10)
    t.right(3)
    t.fd(15)
    t.right(2)
    t.fd(15)
    t.right(2)
    t.fd(15)
    t.circle(-45,200)

def draw_T(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-20,60)
    t.pendown()
    t.fd(80)
    t.goto(20,60)
    t.right(90)
    t.fd(100)

def draw_U(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-20,60)
    t.pendown()
    t.right(90)
    t.fd(80)
    t.circle(45,180)
    t.fd(80)

def draw_V(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-20,60)
    t.pendown()
    t.right(70)
    t.fd(85)
    t.left(140)
    t.fd(85)

def draw_W(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-20,60)
    t.pendown()
    t.right(70)
    t.fd(100)
    t.left(140)
    t.fd(100)
    t.right(140)
    t.fd(100)
    t.left(140)
    t.fd(100)

def draw_X(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-30,60)
    t.pendown()
    t.right(45)
    t.fd(100)
    t.penup()
    t.goto(35,60)
    t.pendown()
    t.right(85)
    t.fd(100)

def draw_Y(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-30,60)
    t.pendown()
    t.right(50)
    t.fd(60)
    t.right(40)
    t.fd(40)
    t.penup()
    t.goto(40,60)
    t.pendown()
    t.right(35)
    t.fd(58)

def draw_Z(t):
    t.speed(1)
    t.pensize(3)
    t.penup()
    t.goto(-30,60)
    t.pendown()
    t.fd(70)
    t.right(133)
    t.fd(100)
    t.left(133)
    t.fd(70)

    




# Initialize turtle
t= turtle.Turtle()


# Set up screen
screen = turtle.Screen()
screen.setup(width=800, height=400)

# Set up turtle properties
t.speed(1) # Speed of drawing
t.pensize(3)  # Pen thickness


# Draw the letters

draw_A(t)
t.reset()
draw_B(t)
t.reset()
draw_C(t)
t.reset()
draw_D(t)
t.reset()
draw_E(t)
t.reset()
draw_F(t)
t.reset()
draw_G(t)
t.reset()
draw_H(t)
t.reset()
draw_I(t)
t.reset()
draw_J(t)
t.reset()
draw_K(t)
t.reset()
draw_L(t)
t.reset()
draw_M(t)
t.reset()
draw_N(t)
t.reset()
draw_O(t)
t.reset()
draw_P(t)
t.reset()
draw_Q(t)
t.reset()
draw_R(t)
t.reset()
draw_S(t)
t.reset()
draw_T(t)
t.reset()
draw_U(t)
t.reset()
draw_V(t)
t.reset()
draw_W(t)
t.reset()
draw_X(t)
t.reset()
draw_Y(t)
t.reset()
draw_Z(t)


# Call other drawing functions for other letters

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()