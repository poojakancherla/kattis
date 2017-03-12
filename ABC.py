ip=[int(x) for x in input().split()]
ip.sort()
A,B,C=ip[0],ip[1],ip[2]
op=input()
s=""
for i in range(len(op)):
    if op[i]=='A':
        s+=str(A)+" "
    elif op[i]=="B":
        s+=str(B)+" "
    elif op[i]=="C":
        s+=str(C)+" "
print(s[:-1])
