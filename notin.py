"""import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Barry,100,10)
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Terry,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)

import turtle
from helpercode import checkpos, intersect, Counter
import random

screen = turtle.Screen()
screen.setworldcoordinates(-400,-400,400,400)

class Runner(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape('turtle')
    self.penup()
    screen.tracer(10)
    self.setpos(-100,0)
    self.seth(0)
    self.pendown()
    screen.tracer(1)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__()

# A list of all of our chasers
chasers = []

class Chaser(turtle.Turtle):
  def __init__(self, target, coordinates = [100,0]):
    turtle.Turtle.__init__(self)
    self.target = target
    self.start = coordinates
    self.shape('turtle')
    c1 = abs(coordinates[0])
    c2 = abs(coordinates[1])
    c3 = max(255, abs(sum(coordinates)))
    self.color(c1, c2, c3)
    self.penup()
    screen.tracer(0)
    self.setpos(self.start)
    self.seth(self.towards(target))
    self.pendown()
    screen.tracer(1)
    # Add Self to list of Chasers
    chasers.append(self)
  def reset(self):
    self.hideturtle()
    self.clear()
    self.__init__(self.target)
  def track(self, move=False):
    screen.tracer(0)
    self.seth(self.towards(self.target) + random.randint(-25,25))
    self.width(self.distance(self.target.pos()) //20)
    if intersect(self.target,self):
      x,y = self.pos()
      c1 = abs(x)
      c2 = abs(y)
      c3 = max(256, abs(sum([x,y])))
      self.color((c1, c2, c3))
      self.penup()
      self.goto(self.start)
      self.pendown()
    elif move:
      self.forward(9+random.randint(-4,0))
    else:
      self.forward(1)
    checkpos([self.target,self],screen)
    screen.tracer(1)

tina = Runner()
tina.write("Click and Drag!")
tina.backward(20)
tommy = Chaser(tina, [200,-50])
sally = Chaser(tina, [50,200])
johnny = Chaser(tina, [-150,-100])

# Reset the game to original state
def reset():
  tina.reset()
  tommy.reset()

# Define functions for each arrow key
def go_left():
  screen.tracer(0)
  tina.left(7)
  tommy.track()
  
def go_right():
  screen.tracer(0)
  tina.right(7)
  tommy.track()
  
def go_forward():
  screen.tracer(0)
  tina.forward(10)
  tommy.track(move=True)
  
def go_backward():
  screen.tracer(0)
  tina.backward(10)
  tommy.track(move=True)
  
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

def drag_function(x,y):
  screen.tracer(0)
  tina.clear()
  tina.goto(x,y)
  for chaser in chasers:
    chaser.track(True)
  screen.tracer(1)

tina.ondrag(drag_function)

# Reset the game when the user presses 'r'
screen.onkey(reset,"r")

# Tell the screen to listen for key presses
screen.listen()
turtle.done() """
# A simple drawing program.
# Click on a color then click on the trinket screen
# to draw lines of that color. The gray color will
# allow you to move the turtle without drawing.
# 
# Patrick Rodriguez, @stratospark

from turtle import *

screen = Screen()
screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

brush_turtle = Turtle()
brush_turtle.goto(0, 0)
brush_turtle.speed(10)
brush_turtle.pensize(20)

# Set up event handler to have the brush_turtle draw a line
# to the point that the user clicks on
def on_screen_click(x, y):
  #print "%d, %d" % (x, y)  
  if y < screenMaxY - 40: # only draw if clicked below color squares
    brush_turtle.goto(x, y)
    
screen.onclick(on_screen_click)
  

class ColorPicker(Turtle):
  def __init__(self, color="red",num=0):
    Turtle.__init__(self)
    self.num = num
    self.color_name = color
    self.speed(0)
    self.shape("circle")
    self.color("black", color)
    self.penup()
    
    # hack to register click handler to instance method
    self.onclick(lambda x, y: self.handle_click(x, y))

  def draw(self):
    self.setx(screenMinX+110+self.num*30)
    self.sety(screenMaxY - 20)
    
  def handle_click(self, x, y):
    if self.color_name == "#F9F9F9":
      brush_turtle.penup()
      brush_turtle.color("black")
    else:
      brush_turtle.pendown()
      brush_turtle.color(self.color_name)
    
# Suppress animations while interface is being drawn
screen.tracer(0)

ui_turtle = Turtle()
ui_turtle.ht()
ui_turtle.penup()
ui_turtle.goto(screenMinX, screenMaxY - 23)
ui_turtle.write("TurtleDraw!", align="left", font=("Courier", 10, "bold"))

# Create color choosing squares at the top of screen
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "#F9F9F9"]
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
  picker.draw()

# Resume animations now that main interface has been drawn
screen.tracer(1)
