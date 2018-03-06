import sys
s = input()

d = {}
l = []


for i in range(0, len(s), 3):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
    if s[i:i+3] in l:
        print("GRESKA")
        sys.exit()
    else:
        l.append(s[i:i+3])

try:
    print(13 - d['P'], end=" ")
except:
    print(13, end = " ")

try:
    print(13 - d['K'], end=" ")
except:
    print(13, end = " ")

try:
    print(13 - d['H'], end=" ")
except:
    print(13, end = " ")

try:
    print(13 - d['T'], end=" ")
except:
    print(13, end = " ")
