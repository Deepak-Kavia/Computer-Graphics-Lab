import matplotlib.pyplot as plt
import numpy as np
import math


df_size = 100
df_x = [0]*100
df_y = [0]*100
df_op = [0]*100
df_penx = 0
df_peny = 0
free = 0

n = int(input("Enter the total no of vertices in the polygon : "))

def put_point(op,x,y):
    global free
    df_op[free] = op
    df_x[free] = x
    df_y[free] =  y
    free = free+1

def move_abs(tx,ty):
    
    global df_penx,df_peny

    df_penx = tx
    df_peny = ty

def do_line(tx,ty):
    global df_peny,df_penx
    tempx = df_penx
    tempy = df_peny 

    df_penx = tx
    df_peny = ty

def rotation():
    angle = float(input("Enter the angle of rotation : "))
    angle = angle * math.pi / 180
    c = math.cos(angle)
    s = math.sin(angle)

    for i in range (0 , n):
        df_x[i] = df_x[i] * c - df_y[i]*s
        df_y[i] = df_x[i] * s + df_y[i]*c

def interpret(xarr,yarr):
    
    for i in range (0,n):
        op = df_op[i]
        tx = df_x[i]
        ty = df_y[i]
        
        if(op == n):
            move_abs(tx,ty)
        elif(op == 2):
            do_line(tx,ty)
        
        xarr.append(df_penx)
        yarr.append(df_peny)

    xarr.append(df_x[0])
    yarr.append(df_y[0])

for i in range(0,n):
    x = int(input("Enter the x coordiante of vertex "))
    y = int(input("Enter the y coordiante of vertex "))

    if(i == 0):
        put_point(n,x,y)
    else:
        put_point(2,x,y)

xarr = []
yarr = []
interpret(xarr,yarr)
rotation()

nxarr = []
nyarr = []
interpret(nxarr,nyarr)

plt.plot(xarr,yarr)
plt.plot(nxarr,nyarr)
plt.show()
