import turtle
import random
red = turtle.Turtle(shape = "turtle")
red.color("red")
yellow = turtle.Turtle(shape = "turtle")
yellow.color("yellow")
green = turtle.Turtle(shape = "turtle")
green.color("green")
blue = turtle.Turtle(shape = "turtle")
blue.color("blue")
pink = turtle.Turtle(shape = "turtle")
pink.color("pink")
orange = turtle.Turtle(shape = "turtle")
orange.color("orange")
performance = turtle.Screen()
performance.setup(width = 500, height = 350)
print(performance.screensize())
colors = {"red": red, "yellow": yellow, "green": green, "blue": blue, "pink": pink, "orange": orange}
color = {"red": "red", "yellow": "yellow", "green": "green", "blue": "blue", "pink": "pink", "orange": "orange"}
coordinate_origin = (performance.canvheight / 2) * -1
for i in colors:
    colors[i].penup()
    colors[i].goto(-190, coordinate_origin + 50)
    coordinate_origin += 50
answer = performance.textinput(title = "Make your bet.", prompt = "Choose your warrior: ").lower()
if answer in colors:
    race_on = True
while race_on == True:
    for i in colors:
        colors[i].forward(random.randint(0,10))
        if colors[i].xcor() >= 230:
            print(f"The {color[i]} turtle wins!")
            if answer == colors[i]:
                print("You win!")
            elif answer != colors[i]:
                print("You lose!")
            race_on = False
performance.exitonclick()