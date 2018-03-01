r, c = map(int, input().split())
parking = [[0 for x in range(r)] for y in range(c)]

def printMatrix(l):
    for i in range(len(l)):
        for x in l[i]:

            print(x, end=' ')
        print()

for i in range(r):
    # parking[i] = list(input())
    parking[i] = input().split(".")


print(parking)
printMatrix(parking)
