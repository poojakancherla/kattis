Alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
Alpha=list(Alpha)
for x in range(30):
    string=input().split()
    # if len(string)==1 and string[0]==0:
    #     break
    # else:
    try:
        i,j = string[0],string[1]
        j=list(j)
        j.reverse()
        s=""
        for a in range(len(j)):
            pos=Alpha.index(j[a])
            pos+=int(i)
            if pos>27:
                pos-=28
            s+=Alpha[pos]

        print(s)
    except:
        break
