sumOfn=0
sumOfodd=0
sumOfeven=0
datasets=int(input())
for i in range(datasets):
    K,N=map(int, input().split())
    sumOfn=(N*(N+1))//2
    sumOfodd=N**2
    sumOfeven=N*(N+1)
    print(K,sumOfn,sumOfodd,sumOfeven)
