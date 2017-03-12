n=input()
for i in range(int(n)):
    guestCount=int(input())
    guestNumber=map(int,input().split())
    guestNumber=list(guestNumber)
    for num in guestNumber:
        if guestNumber.count(num)==1:
            print('Case #'+str(i+1)+': '+str(num))
