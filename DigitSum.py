test=int(input())
for i in range(test):
    indi=[]
    new=[]
    digit=input().split()
    digit=[int(x) for x in digit]
    diff=digit[1]-digit[0]
    TotalSum=0
    IndividualDigitSum=0
    num = 0
    for j in range(diff+1):
        # print(str(digit[0]+j*1))
        num = digit[0]+j*1
        print(num)
        # new.append(digit[0]+j*1)
    # for k in new:
        for digit in str(num):
            IndividualDigitSum+=int(digit)
        TotalSum+=IndividualDigitSum
    print(TotalSum)
