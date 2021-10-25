# Program created by Noam Kabla-Teurtroy and Alexandre Kabla
# 2021

import turtle
import random
import time

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Trake by CosyCody")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score A: 0000  Score B: 0000", align="center", font=("Courier", 24, "normal"))




# Set up players
head_a = turtle.Turtle()
head_a.speed(0)
head_a.shape("square")
head_a.color("blue")
head_a.penup()
head_a.goto(-250,0)
head_a.direction = "up"
head_a.score = 0
head_a.segments = []

head_b = turtle.Turtle()
head_b.speed(0)
head_b.shape("square")
head_b.color("green")
head_b.penup()
head_b.goto(250,0)
head_b.direction = "down"
head_b.score = 0
head_b.segments = []


move_step = 20

def add_segment(segments):
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


# Food items

foodItems = []

def addFoodItem(type):
    if type=="apple": 
        new_food = turtle.Turtle()
        new_food.type="apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("red")
        new_food.penup()
        new_food.goto(random.randint(-300,300),random.randint(-300,300))
        foodItems.append(new_food)


    if type=="golden_apple":
        new_food = turtle.Turtle()
        new_food.type="golden_apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("yellow")
        new_food.penup()
        new_food.goto(random.randint(-300,300),random.randint(-300,300))
        foodItems.append(new_food)
 
    if type=="rotten_apple":
        new_food = turtle.Turtle()
        new_food.type="rotten_apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("blue")
        new_food.penup()
        new_food.goto(random.randint(-300,300),random.randint(-300,300))
        foodItems.append(new_food)

# Detect collision between two turtles
def turt_collision(t1,t2):
    return( (t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2 < 400 )
    
    
    
def go_left(head):
    if head.direction == "up":
        head.direction = "left"
        
    elif head.direction == "left":
        head.direction = "down"
        
    elif head.direction == "down":
        head.direction = "right"
    
    else:
        head.direction = "up"


def go_right(head):
    if head.direction == "up":
        head.direction = "right"
        
    elif head.direction == "right":
        head.direction = "down"
        
    elif head.direction == "down":
        head.direction = "left"
    
    else:
        head.direction = "up"
    
    
    
def go_left_a():
    go_left(head_a)
    
def go_left_b():
    go_left(head_b)
    
def go_right_a():
    go_right(head_a)
    
def go_right_b():
    go_right(head_b)
    
    

def move(head):
   # Move the end segments first in reverse order
    for index in range(len(head.segments)-1, 0, -1):
        x = head.segments[index-1].xcor()
        y = head.segments[index-1].ycor()
        head.segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(head.segments) > 0:
        x = head.xcor()
        y = head.ycor()
        head.segments[0].goto(x,y)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + move_step)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - move_step)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - move_step)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + move_step)
        
        
# Keyboard bindings
wn.listen()
wn.onkeypress(go_left_a, "q")
wn.onkeypress(go_right_a, "w")
wn.onkeypress(go_left_b, "o")
wn.onkeypress(go_right_b, "p")



# Probabilities of the different food items
# 25% apple
# 5%  golden apple
# 10% rotten apple




gametime=0

# Main game loop
while True:
    wn.update()
    move(head_a)
    move(head_b)

    ranu = random.randint(1,100)
    if ranu<=25:
        addFoodItem("apple")
    elif ranu <= 30:
        addFoodItem("golden_apple")
    elif ranu <= 40:
        addFoodItem("rotten_apple")
  
    # handles boundaries
    if head_a.xcor()>290:
       head_a.setx(-290)

    if head_b.xcor()>290:
       head_b.setx(-290)  

    if head_a.xcor()<-290:
       head_a.setx(290)

    if head_b.xcor()<-290:
       head_b.setx(290)  

    if head_a.ycor()>290:
       head_a.sety(-290)

    if head_b.ycor()>290:
       head_b.sety(-290)  

    if head_a.ycor()<-290:
       head_a.sety(290)

    if head_b.ycor()<-290:
       head_b.sety(290)  

   
    # Detect collision with food items

    for food in foodItems:
        for head in [head_a, head_b]:
            if turt_collision(head,food):
                if food.type == "apple":
                    head.score+=1
                if food.type == "golden_apple":
                    head.score+=5
                    add_segment(head.segments)
                if food.type == "rotten_apple":
                    head.score-=1
                food.goto(1000,1000)
 
    



    pen.clear()
    pen.write("Score A: {}  Score B: {}".format(head_a.score, head_b.score), align="center", font=("Courier", 24, "normal")) 


    time.sleep(delay)
    gametime+=1
    
    # Clean up
    if gametime%100==99:
        # filter food item list to remove eaten items
        for i in range(len(foodItems)-1,-1,-1):
            if foodItems[i].xcor()==1000:
                foodItems.pop(i)

        #foodItems = [fooditem for fooditem in foodItems if fooditem.xcor()==1000]
        print(len(foodItems))
  
 


wn.mainloop()
