from graphics import *
from math import*

print("Введите n (чило итераций):")
n=int(input())

window=GraphWin("Снежинка Коха", 800, 600)
window.setBackground('white')

x1=150
y1=150
x2=650
y2=150
x3=400
y3=150+250*sqrt(3)

def koch_curve(x1,y1,x2,y2,x3,y3,n):
    while(n>0):
        lin=Line(Point(x1,y1),Point(x2,y2))
        lin.setFill('yellow')
        lin.draw(window)
        
        x4=x1+(x2-x1)/3
        y4=y1+(y2-y1)/3
        x5=x1+2*(x2-x1)/3
        y5=y1+2*(y2-y1)/3
        #xs=(x1+x2)/2
        #ys=(y1+y2)/2
        xn=(2*(x1+x2)-x3)/3
        yn=(2*(y1+y2)-y3)/3
        point4=Point(x4,y4)
        point5=Point(x5,y5)
        #points=Point(xs,ys)
        pointn=Point(xn,yn)
        
        Line(Point(x1,y1),point4).draw(window)
        Line(point4,pointn).draw(window)
        Line(pointn,point5).draw(window)
        Line(point5,Point(x2,y2)).draw(window)
        
        koch_curve(x4, y4, xn, yn, x5, y5, n-1)
        koch_curve(xn, yn, x5, y5, x4, y4, n-1)
        koch_curve(x1, y1, x4, y4, (2*x1+x3)/3, (2*y1+y3)/3, n-1)
        koch_curve(x5, y5, x2, y2, (2*x2+x3)/3, (2*y2+y3)/3, n-1)
        return n

def koch_snowflake(x1,y1,x2,y2,x3,y3,n):
    point1=Point(x1,y1)
    point2=Point(x2,y2)
    point3=Point(x3,y3)
    
    Line(point1,point2).draw(window)
    Line(point2,point3).draw(window)
    Line(point3,point1).draw(window)
    
    koch_curve(x1,y1,x2,y2,x3,y3,n)
    koch_curve(x2,y2,x3,y3,x1,y1,n)
    koch_curve(x3,y3,x1,y1,x2,y2,n)    

koch_snowflake(x1,y1,x2,y2,x3,y3,n)

window.getMouse()
window.close()