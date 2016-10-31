import turtle
import time

pen = turtle.Turtle()

class Star(object):
    def __init__(self, x=0, y=0, arm_length=2, color="red"):
        """creates a line starting from the coordinates given
        by beg to the coordinates given by end."""
        self.pencolor = color
        self.x = x
        self.y = y
        self.arm_length = arm_length
        self.color=color
        self.tag = "Star"
        self.x1 = x+ arm_length/3.236
        self.y1 = y+ arm_length/2.35

    def __str__(self):
        return "%s x:%s, y:%s, arm:%s, color:%s" % (self.tag,self.x,self.y,self.arm_length, self.color)
    
    def draw(self, pen):
        pen.pencolor(self.color)
        pen.fillcolor(self.color)
        if pen.pos() != (self.x1, self.y1):
            pen.up()
            pen.goto(self.x1, self.y1)
        pen.down()
        pen.begin_fill()
        for i in range(5):
            pen.forward(self.arm_length)
            pen.right(144)
            pen.forward(self.arm_length)
        pen.end_fill()

class Rectangle(object):
    def __init__(self, xc = 0, yc = 0, w =100, h =100, color = "black"):
        self.color = color
        self.x =xc
        self.y =yc
        self.w =w
        self.h = h
        x1=xc-w/2
        y1=yc-h/2
        x2=xc+w/2
        y2=yc+h/2
        self.beg = x1, y1
        self.end = x2, y2
        self.tag = "Rectangle"
    def __str__(self):
        string = "This is a Rectangle with para" + str(self.beg[0])
        return "%s x:%s, y:%s, width:%s, height:%s, color:%s" % (self.tag,self.x,self.y,self.w, self.h,self.color)
    def draw(self, pen):
        pen.pencolor(self.color)
        pen.fillcolor(self.color)
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

class Flag(object):
    def __init__(self, file_object):
        self.rectangles=[];
        self.stars =[];
        self.file_object=file_object
        flag_config_file = open(self.file_object, 'r')
        count=1
        lineNum=1
        starLineNum=1
        for line in flag_config_file.readlines():
            if count==1:
                rectangleNum=line.split(",")
                lineNum=count+int(rectangleNum[0].strip())                
            elif count<=lineNum:
                rectangleConfig=line.split(",")
                drawRectangle = Rectangle(int(rectangleConfig[0].strip()),int(rectangleConfig[1].strip()),int(rectangleConfig[2].strip()),int(rectangleConfig[3].strip()),rectangleConfig[4].strip())
                self.rectangles.append(drawRectangle)
                """print(drawRectangle)"""
                          
            elif count>lineNum and count>starLineNum:
                starNum=line.split(",")
                starLineNum=count+int(starNum[0].strip())                
            elif count<=starLineNum:
                starConfig=line.split(",")
                drawStar = Star(int(starConfig[0].strip()),int(starConfig[1].strip()),int(starConfig[2].strip()),starConfig[3].strip())
                self.stars.append(drawStar)
                """print(drawStar)"""
            
            else:
                break
            count=count+1      
        
        
    def __str__(self):
        string1 = "Rectangles \n"
        string2 = "Stars \n"
        for i in self.rectangles:
            tmp =  " %s \n" % (i)
            string1= string1 + tmp
        
        for j in self.stars:
            tmp =  " %s \n" % (j)
            string2= string2 + tmp
        return  string1+string2
        
    def draw(self, pen):
        for i in self.rectangles: i.draw(pen)
        for j in self.stars: j.draw(pen)
            
        
        
   
        

def main():
    drawFlag = Flag("senegal.txt")
    drawFlag.draw(pen)
    time.sleep(4)
    print(drawFlag)
    
    pen.clear()
    drawFlag = Flag("panama.txt")
    drawFlag.draw(pen)
    print(drawFlag)
    time.sleep(4)

main()

