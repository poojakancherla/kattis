l=[]
total,booked=map(int,input().split())
for i in range(total):
    l.append(i+1)
for i in range(booked):
    bookedrooms=int(input())
    l.remove(bookedrooms)
if total==booked:
    print('too late')
else:
    print(l[0])
