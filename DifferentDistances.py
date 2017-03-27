import math
for i in range(1000):
    s=[float(x) for x in input().split()]
    if not(int(s[0])==0 and len(s)==1):
        x1,y1,x2,y2,p=s[0],s[1],s[2],s[3],s[4]
        dist=(float(x1-x2)**p+(y1-y2)**p)**float(1/p)
        print(abs(dist))
    else:
        break
