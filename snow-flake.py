import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Creative Christmas Snowstorm")
screen.tracer(0)

snowflakes = []
green_colors = ["green", "dark green", "lime green", "forest green", "sea green", "chartreuse"]
for _ in range(50):
    snowflake = turtle.Turtle()
    snowflake.shape("circle")
    snowflake.speed(0)
    snowflake.penup()
    snowflake.shapesize(random.uniform(0.1, 0.3))
    snowflake.goto(random.randint(-400, 400), random.randint(-300, 300))
    snowflakes.append(snowflake)

tree = turtle.Turtle()
tree.color("dark green")
tree.shape("triangle")
tree.shapesize(stretch_wid=10, stretch_len=2)
tree.penup()
tree.goto(0, -250)
for _ in range(3):
    for _ in range(10):
        tree.forward(40)
        tree.stamp()
        tree.backward(40)
        tree.right(36)
    tree.left(120)

snowman = turtle.Turtle()
snowman.shape("circle")
snowman.color("white")
snowman.speed(0)
snowman.penup()
snowman.shapesize(2)
snowman.goto(0, -180)

hat = turtle.Turtle()
hat.shape("triangle")
hat.color("red")
hat.shapesize(stretch_wid=1, stretch_len=2)
hat.penup()
hat.goto(0, -150)

scarf = turtle.Turtle()
scarf.shape("square")
scarf.color("green")
scarf.shapesize(stretch_wid=0.5, stretch_len=3)
scarf.penup()
scarf.goto(-20, -200)

fireworks = []
for _ in range(20):
    firework = turtle.Turtle()
    firework.shape("circle")
    firework.color(random.choice(green_colors))
    firework.speed(0)
    firework.penup()
    firework.goto(random.randint(-400, 400), random.randint(-200, 200))
    firework.attributes = {"dy": random.uniform(3, 6), "gravity": random.uniform(0.1, 0.2)} # type: ignore
    fireworks.append(firework)


def swirl(turtle, angle):
    turtle.right(angle)


while True:
    for snowflake in snowflakes:
        snowflake.color(random.choice(green_colors))
        snowflake.sety(snowflake.ycor() - random.uniform(1, 3))

        if snowflake.ycor() < -350:
            snowflake.goto(random.randint(-400, 400), 300)

        if snowflake.xcor() < -400:
            snowflake.goto(400, snowflake.ycor())

        if snowflake.xcor() > 400:
            snowflake.goto(-400, snowflake.ycor())

        swirl(snowflake, random.randint(-5, 5))

    for firework in fireworks:
        firework.sety(firework.ycor() - firework.attributes["dy"])
        firework.attributes["dy"] -= firework.attributes["gravity"]

        if firework.ycor() < -300:
            firework.goto(random.randint(-400, 400), random.randint(-200, 200))
            firework.attributes = {"dy": random.uniform(3, 6), "gravity": random.uniform(0.1, 0.2)}

    screen.update()