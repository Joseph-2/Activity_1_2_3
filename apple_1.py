#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
def random_location(active_apple):
  ran_x = rand.randint(-150,150)
  ran_y = rand.randint(-50,150)
  active_apple.penup()
  if alphabet:
    active_apple.goto(ran_x,ran_y)
  ind = rand.randint(0,len(alphabet))
  letter = alphabet.pop(ind)
  active_apple.pendown()
#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def write_letter(letter,act_apple):
  x = act_apple.xcor()
  y = act_apple.ycor()
  wn.tracer(False)
  act_apple.penup()
  act_apple.goto(x-5,y-20)
  act_apple.pendown()
  act_apple.color("White")
  act_apple.write(letter,font=("Arial",25,"bold"))
  act_apple.penup()
  act_apple.goto(x,y)
  act_apple.pendown()
  wn.tracer(True)
#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def draw_apple(letter,active_apple):
  active_apple.shape(apple_image)
  write_letter(letter,active_apple)
  wn.update()

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

turtles = []
for i in range(0,5):
  apple = trtl.Turtle()
  turtles.append(apple)
  random_location(apple)

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.
def apple_drop(letter):
  apple.clear()
  xcor = apple.xcor()
  apple.penup()
  apple.goto(xcor,-175)
  random_location(apple)
#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.
def 
#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

#-----function calls----
wn.onkeypress()
wn.listen()
wn.mainloop()