r, c = map(int, input().split())

parking = []

for i in range(r):
    s = list(input())
    l = []
    for i in range(len(s)):
        if s[i] == "#":
            l.append(-4)
        elif s[i]=="X":
            l.append(1)
        else:
            l.append(0)

    parking.append(l)

d = {
    "free" : 0,
    "one" : 0,
    "two" : 0,
    "three" : 0,
    "four" : 0
    }
zero, one,two,three,four = 0,0,0,0,0

for i in range(r-1):
    for j in range(c-1):
        a,b,c1,d = 0,0,0,0

        a = parking[i][j]
        b = parking[i][j+1]
        c1 = parking[i+1][j]
        d = parking[i+1][j+1]

        v = a+b+c1+d

        if v < 0:
            pass
        elif v == 0:
            zero += 1
        elif v == 1:
            one += 1
        elif v == 2:
            two += 1
        elif v == 3:
            three += 1
        elif v == 4:
            four += 1

print(zero)
print(one)
print(two)
print(three)
print(four)
