import math
for i in range(1000):

    r,m,c=map(float, input().split())
    if r==0.0 and m==0.0 and c==0.0:
        break
    else:
        actual_area=math.pi*r**2
        estimate_area=(2*r)**2*(c/m)
        print(actual_area, estimate_area)
