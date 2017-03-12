l=[]
for i in range(5):
    s=0
    grade=[int(x) for x in input().split()]
    for x in grade:
        s+=x
    l.append(s)
print(l)
print((l.index(max(l))+1),max(l))
