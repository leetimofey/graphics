import turtle

size=300
n=5

turtle.penup()
turtle.goto(-size/2, size/3)
turtle.pendown()

tones=['yellow', 'green', 'gold', 'blue', 'brown', 'black']

def koch_curve(size, n):
    if n==0:
        turtle.forward(size)
    else:
        koch_curve(size/3, n-1)
        turtle.left(60)
        koch_curve(size/3, n-1)
        turtle.right(120)
        koch_curve(size/3, n-1)
        turtle.left(60)
        koch_curve(size/3, n-1)

def koch_snowflake(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)
        
turtle.speed(0)

"""koch_snowflake(size, n)"""

for i in range(n+1):
    turtle.color(tones[i])
    koch_snowflake(size, i)

turtle.done()