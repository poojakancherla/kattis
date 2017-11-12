s=input().split()
summ=0
name=""
num=0
for i in range(len(s)):
    try:
        summ+=float(s[i])

        num+=1
    except:
        name+=s[i]+" "

print(summ/num, name[:-1])
