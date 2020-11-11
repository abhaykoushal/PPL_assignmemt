import turtle

s = turtle.getscreen()
t = turtle.Turtle()

class shape:
    def __init__(self, length = 0):        
        self.length = length

class polygon(shape):
    def info(self):
        print("A two-dimensional closed figure with straight sides.")

#shape 1
class line(shape):
    def info(self):
        print("It is a straight line.")
    def show(self):
        t.fd(self.length)

#shape 2
class circle(shape):
    def info(self):
        print("It is a circle.")
    def show(self):
        t.circle(self.length)

#shape 3       
class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

#shape 4       
class square(polygon):
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)

#shape 5     
class rectangle(polygon):
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length/2)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length/2)
        t.rt(90)
    
#shape 6
class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

#shape 7
class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

#shape 8
class heptagon(polygon):
    def show(self):
        for i in range(7):
           t.forward(self.length) 
           t.right(51.43)

#shape 9
class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)

#shape 10
#100 SIDED POLYGON
class hectogon(polygon):
    def show(self):
        for i in range(100):
           t.forward(self.length) 
           t.right(360/100)

shape = octagon(100)
shape.info()
shape.show()






