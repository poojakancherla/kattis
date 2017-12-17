from decimal import Decimal
n = int(input())
for i in range(n):
    scores = [int(x) for x in input().split()]
    num_students = scores[0]
    scores = scores[1:]
    avg = sum(scores)/(num_students)
    count = 0
    for i in scores:
        if i > avg:
            count +=1
    above_avg = Decimal((count * 100)/(num_students))
    print((str(round(above_avg, 3))) + "%")
