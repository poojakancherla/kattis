x,y,z=map(int, input().split())
if x+y==z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'+'+y+'='+z)
elif x==y+z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'='+y+'+'+z)
elif x-y==z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'-'+y+'='+z)
elif x==y-z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'='+y+'-'+z)
elif x/y==z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'/'+y+'='+z)
elif x==y/z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'='+y+'/'+z)
elif x*y==z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'*'+y+'='+z)
elif x==y*z:
    x=str(x)
    y=str(y)
    z=str(z)
    print(x+'='+y+'*'+z)
