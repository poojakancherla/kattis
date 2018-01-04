string = list(input())
l = {}
for i in string:
    if i in l.keys():
        l[i] += 1
    else:
        l[i] = 1
for k,v in l.items():
    if 97<=ord(k) and ord(k)<=122:
        print(k, v)
