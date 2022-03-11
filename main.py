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


red_turtle = RawTurtle(canvas)
red_turtle.color('red')
red_turtle.pu()
red_turtle.speed(50)
red_turtle.left(180)
red_turtle.forward(230)
red_turtle.right(180)


radom_speed_maker = random.randint(1, 10)


def start_button():
    red_turtle.speed(radom_speed_maker),
    red_turtle.forward(250)


btn = tk.Button(root, text='Start the Race')


root.mainloop()
