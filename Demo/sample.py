#//program to draw 2 circles
import turtle
t = turtle.Turtle()
t.circle(50)
t.penup()
t.goto(100,0)
t.pendown()
t.circle(50)
turtle.done()

#// regular expression for phone number validation
import re
def isValid(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)
s = "347873923408"

