import math
from math import radians,sin
h,v=map(int,input().split())
angle=sin(radians(v))
ladder=int(h/angle)
print (ladder+1)
