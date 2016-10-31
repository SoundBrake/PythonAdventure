import turtle
pen = turtle.Turtle()
class Triangle(object):
    def __init__(self, x1 = 0, y1 = 0, x2 = 50, y2 = 50, x3 = 100, y3 = 0, pencolor = "black"):
        """creates a line starting from the coordinates given
        by beg to the coordinates given by end."""
        self.pencolor = pencolor
        self.beg = x1, y1
        self.mid = x2, y2
        self.end = x3, y3
        self.tag = "Triangle"

    def __str__(self):
        string = "This is a Triangle with para" + str(self.beg[0])
        return "%s(%s, %s)" % (self.tag,self.beg,self.end)
    def draw(self, pen):
        pen.pencolor(self.pencolor)
        pen.fillcolor("red")
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.begin_fill()
        pen.goto(self.mid)
        pen.goto(self.end)
        pen.goto(self.beg)
        pen.end_fill()
       # if pen.pos() != self.end
        #    pen.goto(self.end)

class Rectangle(object):
    def __init__(self, x1 = 0, y1 = 0, x2 =100, y2 =100, pencolor = "black"):
        self.pencolor = pencolor
        self.beg = x1, y1
        self.end = x2, y2
        self.tag = "Rectangle"
    def __str__(self):
        string = "This is a Rectangle with para" + str(self.beg[0])
        return "%s(%s, %s)" % (self.tag,self.beg,self.end)
    def draw(self, pen):
        pen.pencolor(self.pencolor)
        pen.fillcolor("blue")
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.begin_fill()
        self.mid1 = self.beg[0], self.end[1]
        self.mid2 = self.end[0],self.beg[1]
        pen.goto(self.mid1)
        pen.goto(self.end)
        pen.goto(self.mid2)
        pen.goto(self.beg)
        pen.end_fill()

class Circle(object):
    def __init__(self, x1 = 0, y1= 0, radius = 10, pencolor = "black"):
        self.pencolor = pencolor
        self.center = x1, y1
        self.radius = float(radius)
        self.tag = "Circle"
    def __str__(self):
        string = "This is a circle with para" + str(self.beg[0])
        return "%s(%s, %s)" % (self.tag,self.beg,self.end)
    def draw(self, pen):
        pen.up()
        pen.goto(self.center)
        pen.fillcolor("yellow")
        pen.down()
        pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()



def main():
    draw_triangle = Triangle(x1 = 0, y1 = 100, x2 = 50, y2 = 150, x3 = 100, y3 = 100, pencolor = "black")
    draw_triangle.draw(pen)
    draw_rectangle = Rectangle()
    draw_rectangle.draw(pen)
    draw_rectangle2 = Rectangle(x1 = 10, x2 =30, y2 = 30)
    draw_rectangle2.draw(pen)
    draw_circle = Circle(x1 = -50, y1= 300, radius = 50, pencolor = "black")
    draw_circle.draw(pen)
    #turtle.resetscreen()

main()

