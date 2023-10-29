import turtle
import random

screen=turtle.Screen()
screen.bgcolor("purple")
screen.title("CatchTheTurtle")
FONT =('Arial', 30, 'normal')
score = 0
turtle_list =[]

#score_turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("yellow")
    score_turtle.penup()
    score_turtle.setposition(0,300)
    score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.penup()
    t.shape("turtle")
    t.shapesize(4)
    t.goto(x, y)
    t.onclick(handle_click)
    turtle_list.append(t)






x_coordinates = [-200,-100,0,100,200]
y_coordinates = [-200,-100,0,100,200]
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()



def show_turtle():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtle,500)






turtle.tracer(0)
setup_score_turtle()

setup_turtles()
hide_turtles()
show_turtle()
turtle.tracer(1)

print(score)
turtle.mainloop()