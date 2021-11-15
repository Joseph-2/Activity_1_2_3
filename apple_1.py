#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
letters = trtl.Turtle()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def apple_fall():
  apple.penup()
  apple.goto(0,-150)
  letters.clear()
  apple.hideturtle()
  apple.goto(0,0)
  apple.showturtle()
def write_letter(letter,color):
  letters.hideturtle()
  x = apple.xcor()
  y = apple.ycor()
  letters.penup()
  letters.goto(x-17,y-40)
  letters.pendown()
  letters.color(color)
  letters.write(letter,font=("Arial",40,"bold"))

#-----function calls-----
draw_apple(apple)
write_letter("A","White")
wn.onkeypress(apple_fall,"a")
wn.listen()
wn.mainloop()