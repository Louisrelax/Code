import math


x1 ,y1 ,x2 ,y2 = (*map(int,input("Enter : ").split( )),)

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(d)