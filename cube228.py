from graphics import *
from math import*
import time

def strnamatr(a,b): #функция умножения строки на матрицу
    x=[]
    for i in range(len(b[0])):
        k=0
        for j in range(len(b)):
            k+=a[j]*b[j][i]
        x.append(k)
    return x

def vectnaint(a,b): #вектор на число
    for i in range(len(a)):
        a[i]=b*a[i]
    return a

def MirovyeVEcrannye(point, fi, teta, ro): #перевод точки из мировых координат в экранные
    point.append(1)
    v=[
        [-sin(teta*pi/180), -cos(fi*pi/180)*cos(teta*pi/180), -sin(fi*pi/180)*cos(teta*pi/180), 0],
        [cos(teta*pi/180), -cos(fi*pi/180)*sin(teta*pi/180), -sin(fi*pi/180)*sin(teta*pi/180), 0],
        [0, sin(fi*pi/180), -cos(fi*pi/180), 0],
        [0, 0, ro, 1]
        ]
    point=strnamatr(point,v)
    del point[-1]
    d=ro/2
    x=[d*point[0]/point[2], d*point[1]/point[2]]
    return x

def MirovyeVVidovye(point, fi, teta, ro): #перевод точки из мировых координат в видовые
    point.append(1)
    v=[
        [-sin(teta*pi/180), -cos(fi*pi/180)*cos(teta*pi/180), -sin(fi*pi/180)*cos(teta*pi/180), 0],
        [cos(teta*pi/180), -cos(fi*pi/180)*sin(teta*pi/180), -sin(fi*pi/180)*sin(teta*pi/180), 0],
        [0, sin(fi*pi/180), -cos(fi*pi/180), 0],
        [0, 0, ro, 1]
        ]
    point=strnamatr(point,v)
    del point[-1]
    return point

def VidovyeVEcrannye(point, ro): #из видовых в экранные
    d=ro/2
    x=[d*point[0]/point[2], d*point[1]/point[2]]
    return x    

def clear(window): #очистка графического окна
    for item in window.items[:]:
        item.undraw()
    window.update()
    
def main(): #каркасная модель
    window=GraphWin("cube", 400, 400)
    window.setBackground('white')
    
    a=100
    vertex=[
        [a, a, a],
        [-a, a, a],
        [-a, -a, a],
        [a, -a, a],
        [a, a, -a],
        [-a, a, -a],
        [-a, -a, -a],
        [a, -a, -a]
        ]
    
    fi=0
    teta=0
    ro=500
    k=0
    while k<1:
        xy=[]
        for i in range (len(vertex)):
            xy.append(MirovyeVEcrannye(vertex[i], fi, teta, ro))
        lin1=Line(Point(xy[0][0]+200, xy[0][1]+200), Point(xy[1][0]+200, xy[1][1]+200))
        lin1.draw(window)
        lin2=Line(Point(xy[1][0]+200, xy[1][1]+200), Point(xy[2][0]+200, xy[2][1]+200))
        lin2.draw(window)
        lin3=Line(Point(xy[2][0]+200, xy[2][1]+200), Point(xy[3][0]+200, xy[3][1]+200))
        lin3.draw(window)
        lin4=Line(Point(xy[3][0]+200, xy[3][1]+200), Point(xy[0][0]+200, xy[0][1]+200))
        lin4.draw(window)
        lin5=Line(Point(xy[4][0]+200, xy[4][1]+200), Point(xy[5][0]+200, xy[5][1]+200))
        lin5.draw(window)
        lin6=Line(Point(xy[5][0]+200, xy[5][1]+200), Point(xy[6][0]+200, xy[6][1]+200))
        lin6.draw(window)
        lin7=Line(Point(xy[6][0]+200, xy[6][1]+200), Point(xy[7][0]+200, xy[7][1]+200))
        lin7.draw(window)
        lin8=Line(Point(xy[7][0]+200, xy[7][1]+200), Point(xy[4][0]+200, xy[4][1]+200))
        lin8.draw(window)
        lin9=Line(Point(xy[0][0]+200, xy[0][1]+200), Point(xy[4][0]+200, xy[4][1]+200))
        lin9.draw(window)
        lin10=Line(Point(xy[1][0]+200, xy[1][1]+200), Point(xy[5][0]+200, xy[5][1]+200))
        lin10.draw(window)
        lin11=Line(Point(xy[2][0]+200, xy[2][1]+200), Point(xy[6][0]+200, xy[6][1]+200))
        lin11.draw(window)
        lin12=Line(Point(xy[3][0]+200, xy[3][1]+200), Point(xy[7][0]+200, xy[7][1]+200))
        lin12.draw(window)
        
        fi+=2
        teta+=3
        time.sleep(0.1)
        clear(window)
    window.getMouse()
    window.close()

def main2(): #закраска граней по первому алгоритму
    window=GraphWin("cube", 400, 400)
    window.setBackground('white')
    
    a=100
    vertex=[
        [a, a, a],
        [-a, a, a],
        [-a, -a, a],
        [a, -a, a],
        [a, a, -a],
        [-a, a, -a],
        [-a, -a, -a],
        [a, -a, -a]
        ]
    edges=[
        [0,3,7,4],
        [3,0,1,2], #лицевая
        [3,2,6,7],
        [2,1,5,6],
        [1,0,4,5],
        [5,4,7,6]
        ]
    colors=[
        'red',
        'orange',
        'yellow',
        'pink',
        'green',
        'blue'
        ]
    
    fi=0
    teta=0
    ro=500
    check=0
    while check<1:
        xy=[]
        for i in range (len(vertex)):
            xy.append(MirovyeVVidovye(vertex[i], fi, teta, ro))
        for i in range(len(edges)):
            gran=[]
            for j in range(len(edges[i])):
                gran.append(xy[edges[i][j]])
            V1=gran[0]
            V2=gran[1]
            V3=gran[2]
            a=(V2[1]-V1[1])*(V3[2]-V1[2])-(V2[2]-V1[2])*(V3[1]-V1[1])
            b=(V3[0]-V1[0])*(V2[2]-V1[2])-(V2[0]-V1[0])*(V3[2]-V1[2])
            c=(V2[0]-V1[0])*(V3[1]-V1[1])-(V2[1]-V1[1])*(V3[0]-V1[0])
            d=-1*(V1[0]*a+V1[1]*b+V1[2]*c)
            if d<0: #(a*gran[3][0]+b*gran[3][1]+c*gran[3][2])>=0:
                vidov=[]
                for k in range(len(gran)):
                    vidov.append(VidovyeVEcrannye(gran[k], ro))
                edge=Polygon(Point(vidov[0][0]+200, vidov[0][1]+200), Point(vidov[1][0]+200, vidov[1][1]+200), Point(vidov[2][0]+200, vidov[2][1]+200), Point(vidov[3][0]+200, vidov[3][1]+200))
                edge.setFill(colors[i])
                edge.draw(window)
        fi+=2
        teta+=3
        time.sleep(0.1)
        clear(window)
    window.getMouse()
    window.close()

def main3(): #закраска граней по второму алгоритму
    window=GraphWin("cube", 400, 400)
    window.setBackground('white')
    
    a=100
    vertex=[
        [a, a, a],
        [-a, a, a],
        [-a, -a, a],
        [a, -a, a],
        [a, a, -a],
        [-a, a, -a],
        [-a, -a, -a],
        [a, -a, -a]
        ]
    edges=[
        [0,3,7,4],
        [3,0,1,2],
        [3,2,6,7],
        [2,1,5,6],
        [1,0,4,5],
        [5,4,7,6]
        ]
    colors=[
        'red',
        'orange',
        'yellow',
        'pink',
        'green',
        'blue'
        ]
    
    fi=0
    teta=0
    ro=500
    check=0
    while check<1:
        xy=[]
        for i in range (len(vertex)):
            xy.append(MirovyeVVidovye(vertex[i], fi, teta, ro))
        xk=0
        yk=0
        zk=0
        for i in range(len(xy)):
            xk+=xy[i][0]/8
            yk+=xy[i][1]/8
            zk+=xy[i][2]/8
        for i in range(len(edges)):
            gran=[]
            for j in range(len(edges[i])):
                gran.append(xy[edges[i][j]])
            V1=gran[0]
            V2=gran[1]
            V3=gran[2]
            V4=gran[3]
            xg=(V1[0]+V2[0]+V3[0]+V4[0])/4
            yg=(V1[1]+V2[1]+V3[1]+V4[1])/4
            zg=(V1[2]+V2[2]+V3[2]+V4[2])/4
            vectd=[xg,yg,zg]
            
            a=(V2[1]-V1[1])*(V3[2]-V1[2])-(V2[2]-V1[2])*(V3[1]-V1[1])
            b=(V3[0]-V1[0])*(V2[2]-V1[2])-(V2[0]-V1[0])*(V3[2]-V1[2])
            c=(V2[0]-V1[0])*(V3[1]-V1[1])-(V2[1]-V1[1])*(V3[0]-V1[0])
            d=-V1[0]*a-V1[1]*b-V1[2]*c
            vecte=[a,b,c]
            if (a*xk+b*yk+c*zk+d)<0:
                vecte=vectnaint(vecte,-1)
            cosGamma=(vectd[0]*vecte[0]+vectd[1]*vecte[1]+vectd[2]*vecte[2])/(sqrt((vectd[0]**2+vectd[1]**2+vectd[2]**2)*(vecte[0]**2+vecte[1]**2+vecte[2]**2)))
            if cosGamma>0:
                vidov=[]
                for k in range(len(gran)):
                    vidov.append(VidovyeVEcrannye(gran[k], ro))
                edge=Polygon(Point(vidov[0][0]+200, vidov[0][1]+200), Point(vidov[1][0]+200, vidov[1][1]+200), Point(vidov[2][0]+200, vidov[2][1]+200), Point(vidov[3][0]+200, vidov[3][1]+200))
                edge.setFill(colors[i])
                edge.setOutline(colors[i])
                edge.draw(window)
        fi+=2
        teta+=3
        time.sleep(0.1)
        clear(window)
    window.getMouse()
    window.close()    

start=int(input())
if start==1:
    main()
if start==2:
    main2()
if start==3:
    main3()