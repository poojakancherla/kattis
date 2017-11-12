import sys
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
s=list(s)
for i in range(30):
    inp = input()
    if inp == "0":
        sys.exit()
    k,n=inp.split()
    k=int(k)
    n=list(n)
    na=[]
    for x in n:
        i=s.index(x)
        if i+k>=28:
            na.append(s[i+k-28])
        if i+k<=27:
            na.append(s[i+k])
    na.reverse();
    na = ''.join(na)
    print(na)
