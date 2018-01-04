statues = int(input())
printer = 1
days = 0
if statues == 1:
    print(1)
else:
    while(printer < statues/2):
        printer = printer * 2
        days += 1
    print(days + 2)
