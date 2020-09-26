import turtle

#Learning to use Python turtle Graphics from Tech WithT im https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg

cake = turtle.Turtle()
cake.color('red')
cake.pensize(5)
cake.shape('turtle')

cake.forward(100)
cake.left(90)
cake.penup()
cake.backward(100)
cake.right(90)
cake.pendown()
cake.forward(100)
cake.color('green')


crab = turtle.Turtle()
crab.color("blue")
crab.pensize(5)
crab.shape('turtle')

crab.right(90)
crab.backward(100)
crab.right(90)
crab.pendown()
crab.forward(100)
crab.color('red')

# Decided this is NOT my cup of tea, moving on to PyGame