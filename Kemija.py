ip=input()
op=""

i=0
while i <len(ip):
    c=ip[i]
    if c in 'aeiou':
        op=op+c
        i=i+2
    else:
        op=op+c
    i+=1
print(op)
