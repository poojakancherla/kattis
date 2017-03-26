x= int(input())
n=int(input())
total=0
for i in range(n):
    pi=int(input())
    total=total+pi
available=(n+1)*x-total
print(available)
