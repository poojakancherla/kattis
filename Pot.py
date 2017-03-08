n=input()
s=0
for i in range(int(n)):
    num=input()
    # print(num)
    s=s+(int(num[:-1])**int(num[-1]))
print(s)
