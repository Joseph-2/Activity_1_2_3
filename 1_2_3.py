#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

turtles = []
for x in range(0,5):
    apple = trtl.Turtle()
    turtles.append(apple)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ind = rand.randint(0,25)
letter = alphabet.pop(ind)
#------functions-----------
def random_location(active_apple):
    ran_x = rand.randint(-150,150)
    ran_y = rand.randint(-50,150)
    active_apple.penup()
    active_apple.goto(ran_x,ran_y)
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()
def write_letter(letterz,act_apple):
    x = act_apple.xcor()
    y = act_apple.ycor()
    wn.tracer(False)
    act_apple.penup()
    act_apple.goto(x-5,y-20)
    act_apple.pendown()
    act_apple.color("White")
    act_apple.write(letterz,font=("Arial",25,"bold"))
    act_apple.penup()
    act_apple.goto(x,y)
    act_apple.pendown()
    wn.tracer(True)
def apple_fall(active_apple,x):
    xcor = active_apple.xcor()
    active_apple.penup()
    active_apple.goto(xcor,-150)
    active_apple.hideturtle()
    random_location(active_apple)
    active_apple.showturtle()

#------function_calls--------
for x in turtles:

    draw_apple(x)
    random_location(x)
    write_letter(letter,x)
wn.onkeypress(apple_fall,letter)
wn.listen()
wn.mainloop()