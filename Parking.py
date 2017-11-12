import math
cases=int(input())
# numbers
for i in range(cases):
    stores=int(input())
    numbers=[int(x) for x in input().split()]
# print(numbers)
    numbers.sort()
    print(2*(numbers[-1]-numbers[0]))
