from turtle import *
t = Turtle()
screen = t.getscreen()
t.forward(300)

def writeName():
	name = screen.textinput("name box", "What is your name?")
	t.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()

screen.onkey(writeName, "w")

screen.listen()
screen.mainloop()