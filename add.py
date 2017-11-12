size=int(input())
a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
result=[]
for i in range(size):
    result.append(str(a[i]+b[i]))

d=" ".join(result)
print(d)
