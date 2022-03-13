<<<<<<< HEAD
import tkinter as tk
from turtle import ScrolledCanvas, Turtle, Screen, RawTurtle
from turtle import *
from random import randint
from weakref import ref

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry('600x600')
canvas = ScrolledCanvas(root)
canvas.pack()


# Ref Turtle
ref_turtle = RawTurtle(canvas)
ref_turtle.color('black')
ref_turtle.pu()
ref_turtle.speed(5)
ref_turtle.left(90)
ref_turtle.forward(150)
ref_turtle.right(90)
ref_turtle.forward(180)
ref_turtle.right(90)
ref_turtle.pd()
ref_turtle.forward(300)
ref_turtle.right(90)
ref_turtle.forward(410)
ref_turtle.right(90)
ref_turtle.forward(300)
ref_turtle.right(90)
ref_turtle.forward(410)

ref_turtle.ht()

# Red Turtle
red_turtle = RawTurtle(canvas)
red_turtle.color('red')
red_turtle.pu()
red_turtle.speed(1)
red_turtle.left(180)
red_turtle.forward(230)
red_turtle.right(180)


# Blue Turtle
blue_turtle = RawTurtle(canvas)
blue_turtle.color('blue')
blue_turtle.pu()
blue_turtle.speed(1)
blue_turtle.left(180)
blue_turtle.forward(230)
blue_turtle.right(90)
blue_turtle.forward(30)
blue_turtle.right(90)


# Green Turtle
green_turtle = RawTurtle(canvas)
green_turtle.color('green')
green_turtle.pu()
green_turtle.speed(1)
green_turtle.left(180)
green_turtle.forward(230)
green_turtle.right(90)
green_turtle.forward(60)
green_turtle.right(90)


# Black Turtle
black_turtle = RawTurtle(canvas)
black_turtle.color('black')
black_turtle.pu()
black_turtle.speed(1)
black_turtle.left(180)
black_turtle.forward(230)
black_turtle.left(90)
black_turtle.forward(30)
black_turtle.right(-90)


def start_race():
    for turn in range(130):
        black_turtle.forward(randint(1, 5))
        red_turtle.forward(randint(1, 5))
        blue_turtle.forward(randint(1, 5))
        green_turtle.forward(randint(1, 5))


btn = tk.Button(root, text='Start the Race', command=start_race)
btn.pack()


root.mainloop()
=======
import tkinter as tk
import random
from turtle import ScrolledCanvas, Turtle, Screen, RawTurtle
import turtle

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry('600x600')
canvas = ScrolledCanvas(root)
canvas.pack()

# Red Turtle
red_turtle = RawTurtle(canvas)
red_turtle.color('red')
red_turtle.pu()
red_turtle.speed(1)
red_turtle.left(180)
red_turtle.forward(230)
red_turtle.right(180)


# Blue Turtle
blue_turtle = RawTurtle(canvas)
blue_turtle.color('blue')
blue_turtle.pu()
blue_turtle.speed(1)
blue_turtle.left(180)
blue_turtle.forward(230)
blue_turtle.right(90)
blue_turtle.forward(30)
blue_turtle.right(90)


# Green Turtle
green_turtle = RawTurtle(canvas)
green_turtle.color('green')
green_turtle.pu()
green_turtle.speed(1)
green_turtle.left(180)
green_turtle.forward(230)
green_turtle.right(90)
green_turtle.forward(60)
green_turtle.right(90)


# Black Turtle
black_turtle = RawTurtle(canvas)
black_turtle.color('black')
black_turtle.pu()
black_turtle.speed(1)
black_turtle.left(180)
black_turtle.forward(230)
black_turtle.left(90)
black_turtle.forward(30)
black_turtle.right(-90)


# Black Turtle
black_turtle = RawTurtle(canvas)
black_turtle.color('black')
black_turtle.pu()
black_turtle.speed(1)
black_turtle.left(180)
black_turtle.forward(230)
black_turtle.left(90)
black_turtle.forward(30)
black_turtle.right(-90)

radom_speed_maker = random.randint(1, 10)


def start_button():
    red_turtle.speed(radom_speed_maker),
    red_turtle.forward(450)
    blue_turtle.speed(radom_speed_maker),
    blue_turtle.forward(450)


btn = tk.Button(root, text='Start the Race', command=start_button)
btn.pack()

root.mainloop()
>>>>>>> c7db7be8c77942652955a53aa6cbd9192e3afc0a
