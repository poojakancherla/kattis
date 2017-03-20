N=int(input())
l=[]
for i in range(N):
    color,radius=map(str,input().split())
    try:
        radius=int(radius)
        l.append((radius,color))
    except:
        colTemp=radius
        radTemp=int(color)
        radTemp/=2
        color=colTemp
        radius=int(radTemp)
        l.append((radius,color))
l.sort()
for x in l:
    print(x[1])
