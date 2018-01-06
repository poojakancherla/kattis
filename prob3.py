nums = [135678, 5678, 2345, 6453]
nc = 0
for i in nums:
    count = 0
    i = [int(x) for x in str(i)]
    for j in range(len(i) - 1):
        if i[j] < i[j+1]:
            count += 1
        else:
            break
    if count == len(i)-1:
        nc += 1

print(nc)
