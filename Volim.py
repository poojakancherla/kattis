K=int(input())
N=int(input())
time_left=210
for i in range(N):
    time,Z=input().split()
    time_left=time_left-int(time)
    if time_left<=0:
        break
    if Z=='N' or Z=='P':
        continue
    else:
        if K==8:
            K=1
        else:
            K+=1
print(K)
