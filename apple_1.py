#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file


letters = ["A","B","C","D","E","F","G","H","I"]
apple_letters = []
turtles = []

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
def random_location(turtle_index):
  ran_x = rand.randint(-150,150)
  ran_y = rand.randint(-50,150)
  turtles[turtle_index].penup()
  turtles[turtle_index].goto(ran_x,ran_y)
  turtles[turtle_index].pendown()
  ind = rand.randint(0,len(letters)-1)
  apple_letters.append(letters.pop(ind))
#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def write_letter(turtle_index):
  x = turtles[turtle_index].xcor()
  y = turtles[turtle_index].ycor()
  wn.tracer(False)
  turtles[turtle_index].penup()
  turtles[turtle_index].goto(x-5,y-20)
  turtles[turtle_index].pendown()
  turtles[turtle_index].color("White")
  turtles[turtle_index].write(apple_letters[turtle_index],font=("Arial",25,"bold"))
  turtles[turtle_index].penup()
  turtles[turtle_index].goto(x,y)
  turtles[turtle_index].pendown()
  wn.tracer(True)
#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def draw_apple(turtle_index):
  turtles[turtle_index].shape(apple_image)
  write_letter(turtle_index)
  wn.update()
#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0,5):
  apple = trtl.Turtle()
  turtles.append(apple)
  random_location(i)
  draw_apple(i)

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.
def apple_drop(letter_index):
  turtles[letter_index].clear()
  turtles[letter_index].penup()
  turtles[letter_index].sety(-150)
  turtles[letter_index].hideturtle()
#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.
def typed_A():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "A":
      apple_drop(x)
def typed_B():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "B":
      apple_drop(x)
def typed_C():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "C":
      apple_drop(x)
def typed_D():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "D":
      apple_drop(x)
def typed_E():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "E":
      apple_drop(x)
def typed_F():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "F":
      apple_drop(x)
def typed_G():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "G":
      apple_drop(x)
def typed_H():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "H":
      apple_drop(x)
def typed_I():
  for x in range(0,len(turtles)):
    if apple_letters[x] == "I":
      apple_drop(x)
#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
#-----function calls----
wn.onkeypress(typed_A,"a")
wn.onkeypress(typed_B,"b")
wn.onkeypress(typed_C,"c")
wn.onkeypress(typed_D,"d")
wn.onkeypress(typed_E,"e")
wn.onkeypress(typed_F,"f")
wn.onkeypress(typed_G,"g")
wn.onkeypress(typed_H,"h")
wn.onkeypress(typed_I,"i")
wn.listen()
wn.mainloop()