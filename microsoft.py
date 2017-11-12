n=int(input())
objects=[1,2,3]
shading=['E', 'S', 'F']
color=['R', 'P', 'G']
shape=['O', 'S', 'D']
for i in range(n):
    ip=input().split()
    first=list(ip[0])
    second=list(ip[1])
    for j in range(4):
        if first[0]==second[0]:
            third[0]=first[0]
        else:
            objects.remove(first[0],second[0])
            third[0]=objects[0]
print(third[0])
