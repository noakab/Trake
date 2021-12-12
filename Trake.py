# Program created by Noam Kabla-Teurtroy and Alexandre Kabla
# 2021

import turtle
import random
import time

delay = 0.1

arena_height=500
arena_width=600
window_height=arena_height+100
window_width=arena_width+100
# Set up the screen
wn = turtle.Screen()
wn.title("Trake by CosyCody")
wn.bgcolor("orange")

wn.setup(window_width,window_height)
wn.tracer(0) # Turns off the screen updates

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
#1212
border_pen.setposition(-arena_width/2,-arena_height/2)
border_pen.pendown()
border_pen.pensize(3)
#for side in range(4):

border_pen.fd(arena_width)
border_pen.lt(90)
border_pen.fd(arena_height)
border_pen.lt(90)
border_pen.fd(arena_width)
border_pen.lt(90)
border_pen.fd(arena_height)
border_pen.lt(90)
border_pen.hideturtle()	



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, window_height/2-40)
pen.write("Score A: 0000  Score B: 0000", align="center", font=("Courier", 24, "normal"))




# Set up players
head_a = turtle.Turtle()
head_a.speed(0)
head_a.shape("square")
head_a.color("blue")
head_a.penup()
head_a.goto(-arena_width/2+50,0)
head_a.direction = "right"
head_a.score = 0
head_a.segments = []

head_b = turtle.Turtle()
head_b.speed(0)
head_b.shape("square")
head_b.color("green")
head_b.penup()
head_b.goto(arena_width/2-50,0)
head_b.direction = "left"
head_b.score = 0
head_b.segments = []


move_step = 20

def add_segment(head):
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        if len(head.segments)>0:
            segment_number=len(head.segments)-1
            x = head.segments[segment_number].xcor()
            y = head.segments[segment_number].ycor()
            new_segment.goto(x,y)
        else:
            new_segment.goto(window_width,window_height)
        head.segments.append(new_segment)


# Food items
structureList = []
foodItems = []
mobsList = []


def addFoodItem(type,x,y):
    if type=="apple": 
        new_food = turtle.Turtle()
        new_food.type="apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("red")

    if type=="golden_apple":
        new_food = turtle.Turtle()
        new_food.type="golden_apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("yellow")
 
    if type=="rotten_apple":
        new_food = turtle.Turtle()
        new_food.type="rotten_apple"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("blue")
        
    if type=="black_berry":
        new_food = turtle.Turtle()
        new_food.type="black_berry"
        new_food.speed(0)
        new_food.shape("triangle")
        new_food.color("black")

    if type=="chaos_berry": 
        new_food = turtle.Turtle()
        new_food.type="chaos_berry"
        new_food.speed(0)
        new_food.shape("circle")
        new_food.color("black")

    new_food.penup()
    new_food.goto(x,y)
    foodItems.append(new_food)
    
 

def addMob(type,x,y):
    if type=="scarabet": 
        new_mob = turtle.Turtle()
        new_mob.type="scarabet"
        new_mob.speed(0)
        new_mob.shape("triangle")
        new_mob.color("red")
    new_mob.penup()
    new_mob.goto(x,y)
    mobsList.append(new_mob)

def addstructure(type,x,y):
    if type=="portal": 
        new_structure = turtle.Turtle()
        new_structure.type="portal"
        new_structure.speed(0)
        new_structure.shape("square")
        new_structure.color("brown")
        
    new_structure.penup()
    new_structure.goto(x,y)
    structureList.append(new_structure)




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
 

def drop_segments(head):
    for index in range(len(head.segments)-1, -1, -1):
        x = head.segments[index].xcor()
        y = head.segments[index].ycor()
        head.segments[index].goto(window_width,window_height)
        head.segments.pop(index)
        head.score -= 5
        addFoodItem("golden_apple",x,y)







        
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

addstructure("portal",130,120)
addstructure("portal",130,-120)
addstructure("portal",-130,120)
addstructure("portal",-130,-120)
gametime=0

# Main game loop
while gametime<1500:
    wn.update()
    move(head_a)
    move(head_b)
#1212 1212 1212 1212
    ranu = random.randint(1,50)
    if ranu<=10:
        addFoodItem("apple",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    elif ranu <= 15:
        addFoodItem("golden_apple",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    elif ranu <= 20:
        addFoodItem("rotten_apple",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    elif ranu <= 30:
        addMob("scarabet",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    elif ranu <= 31:
        addFoodItem("black_berry",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    elif ranu <= 32:
        addFoodItem("chaos_berry",random.randint(-arena_width/2,arena_width/2),random.randint(-arena_height/2,arena_height/2))
    
    # handles boundaries
    for head in [head_a, head_b]:
        if head.xcor()>arena_width/2-10:
           head.setx(-arena_width/2+10)
           drop_segments(head)

        if head.xcor()<-arena_width/2+10:
           head.setx(arena_width/2-10)
           drop_segments(head)

        if head.ycor()>arena_height/2-10:
           head.sety(-arena_height/2+10)
           drop_segments(head)

        if head.ycor()<-arena_height/2+10:
           head.sety(arena_height/2-10)
           drop_segments(head)

  
    # Move mobs

    for mob in mobsList:
        if mob.xcor()!=1000:
            x=(mob.xcor()+random.randint(-15,15) +arena_width/2 )%(arena_width) -arena_width/2
            y=(mob.ycor()+random.randint(-15,15) +arena_height/2 )%arena_height -arena_height/2
            mob.tilt(random.randint(-15,15))
            mob.goto(x,y)


    # Detect collision with food items

    for food in foodItems:
        for head in [head_a, head_b]:
            if turt_collision(head,food):
                if food.type == "apple":
                    head.score+=1
                if food.type == "golden_apple":
                    head.score+=5
                    add_segment(head)
                if food.type == "rotten_apple":
                    head.score-=1
                food.goto(1000,1000)
                
                if food.type == "black_berry":
                    head.score-=5
                    drop_segments(head)                 #add_segment(head.segments)
                food.goto(1000,1000)
                
                if food.type == "chaos_berry":
                    head.score-=0
                    for i in range(5):
                        add_segment(head)
                food.goto(arena_width,arena_height)
               # if food.type == "":
                    #head.score-=0
                   # for i in range(5):
                        #add_segment(head)
                #food.goto(arena_width,arena_height)
 
    for mob in mobsList:
        for head in [head_a, head_b]:
            if turt_collision(head,mob):
                if mob.type == "scarabet":
                    head.score+=1
                mob.goto(1000,1000)
 
    
    for head in [head_a, head_b]:
        for head2 in [head_a, head_b]:
            for segment in head2.segments:
                if turt_collision(head,segment):
                    drop_segments(head)               


    for structure in structureList:
        for head in [head_a, head_b]:
            if turt_collision(head,structure):
                if structure.type == "portal":
                    head.score+=20
                    head.goto(0,0)
    pen.clear()
    pen.write("Score A: {}  Score B: {}".format(head_a.score, head_b.score), align="center", font=("Courier", 24, "normal")) 


    time.sleep(delay)
    gametime+=1
    
    # Clean up
    if gametime%100==99:
        # filter food item list to remove eaten items
        for i in range(len(foodItems)-1,-1,-1):
            if foodItems[i].xcor()==window_width:
                foodItems.pop(i)
        for i in range(len(mobsList)-1,-1,-1):
            if mobsList[i].xcor()==window_width:
                mobsList.pop(i)


        #foodItems = [fooditem for fooditem in foodItems if fooditem.xcor()==1000]
        print(len(foodItems))
  
 

print("Score A: {}  Score B: {}".format(head_a.score, head_b.score))         
#wn.mainloop()
