s=input()
if len(s)>=1 and len(s)<=100000:
    s=list(s)
    ws=s.count('_')
    l=0
    sym=0
    u=0
    for x in s:
        if 97<=ord(x)<=122:
            l+=1
        elif 65<=ord(x)<=90:
            u+=1
        elif 33<=ord(x)<=64 or 91<=ord(x)<=96 or 123<=ord(x)<=126:
            sym+=1
    sym=sym-ws
    # print(l,u,ws,sym)
    ratio_ws=ws/len(s)
    ratio_l=l/len(s)
    ratio_u=u/len(s)
    ratio_sym=sym/len(s)
    print(ratio_ws)
    print(ratio_l)
    print(ratio_u)
    print(ratio_sym)
