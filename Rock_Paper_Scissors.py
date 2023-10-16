#  Graphics library for functions being displayed (turtle)
import turtle
from turtle import *
from random import randint

choices = ["rock", "paper", "scissors"]
cpuchoice = choices[randint(0,2)]

# The os module allows us to access the current directory in order to access assets
import os

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# setting variables for image length and height for hitbox determination
rock_w = 154
rock_h = 170
paper_w = 241
paper_h = 157
scissors_w = 256
scissors_h = 170

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="light blue")

#Text printed on the screen
def write_text(message, x, y):
    text = turtle.Turtle()
    text.color('black')
    text.penup()
    text.setpos(x,y)
    text.hideturtle()
    text.write(message, False, "center", ("Arial", 22, "bold"))


#Calling the Function above
write_text("Please choose rock, paper, or scissors", 0, 150)

# setup the rock image using the os module as rock_image

rock_image = os.path.join(images_folder, 'rock.gif')
cpu_rock = os.path.join(images_folder, 'cpu_rock.gif')

paper_image = os.path.join(images_folder, 'paper.gif')
cpu_paper = os.path.join(images_folder, 'cpu_paper.gif')

scissors_image = os.path.join(images_folder, 'scissors.gif')
cpu_scissors = os.path.join(images_folder, 'cpu_scissors.gif')

# instantiate (create an instance of) the Turtle class for the rock

#Rock Instance
rock_instance = turtle.Turtle()
cpu_rock_instance = turtle.Turtle()
cpu_rock_instance.hideturtle()
cpu_rock_instance.penup()

#Paper Instance
paper_instance = turtle.Turtle()
cpu_paper_instance = turtle.Turtle()
cpu_paper_instance.hideturtle()
cpu_paper_instance.penup()

#Scissors Instance
scissors_instance = turtle.Turtle()
cpu_scissors_instance = turtle.Turtle()
cpu_scissors_instance.hideturtle()
cpu_scissors_instance.penup()


#Display screen 
screen.addshape(rock_image)
screen.addshape(paper_image)
screen.addshape(scissors_image)
screen.addshape(cpu_rock)
screen.addshape(cpu_paper)
screen.addshape(cpu_scissors)

# attach the rock_image to the rock_instance

rock_instance.shape(rock_image)
paper_instance.shape(paper_image)
scissors_instance.shape(scissors_image)
cpu_rock_instance.shape(cpu_rock)
cpu_paper_instance.shape(cpu_paper)
cpu_scissors_instance.shape(cpu_scissors)
cpu_scissors_instance.hideturtle()
cpu_scissors_instance.penup()

rock_pos_x = -300
rock_pos_y = 0
paper_pos_x = 0
paper_pos_y = 0
scissors_pos_x = 300
scissors_pos_y = 0

rock_instance.penup()
paper_instance.penup()
scissors_instance.penup()


rock_instance.setpos(rock_pos_x,rock_pos_y)
paper_instance.setpos(paper_pos_x, paper_pos_y)
scissors_instance.setpos(scissors_pos_x, scissors_pos_y)

# remove the pen option from the rock_instance so it doesn't draw lines when moved
def collide(x,y,obj,w,h):

    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

userchoice = "nothing"

# defining a function where if we click the image on the screen we send a message to terminal to correlate.
def mouse_pos(x, y):
    if collide(x,y,rock_instance,rock_w,rock_h):
        userchoice = "rock"
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        if cpuchoice == "paper":
            print("You lost")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "rock":
            print("You tie")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "scissors":
            print("You win")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
    elif collide(x,y,paper_instance,paper_w,paper_h):
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "paper"
        if cpuchoice == "paper":
            print("You tie")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "rock":
            print("You win")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "scissors":
            print("You lose")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        paper_instance.hideturtle()
        rock_instance.hideturtle()
        scissors_instance.setpos(rock_pos_x, rock_pos_y)
        userchoice = "scissors"
        if cpuchoice == "paper":
            print("You won")
            cpu_paper_instance.showturtle()
            cpu_paper_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "rock":
            print("You lost")
            cpu_rock_instance.showturtle()
            cpu_rock_instance.setpos(scissors_pos_x, scissors_pos_y)
        elif cpuchoice == "scissors":
            print("You tie")
            cpu_scissors_instance.showturtle()
            cpu_scissors_instance.setpos(scissors_pos_x, scissors_pos_y)
    else:
        userchoice = "nothing"
        print("choose something")

screen.onclick(mouse_pos)

# have the turtle module 'listen' for when keys are pressed
turtle.listen()

# when the turtle 'x' key is pressed then quit turtle
turtle.done()

 