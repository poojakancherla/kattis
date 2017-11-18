n = int(input())




sequence = [int(x) for x in input().split()]
left = sequence[0]
gis = [left]

count = 1
for j in range(1, len(sequence)):

    if left < sequence[j]:
        gis.append(sequence[j])
        count += 1
        left = sequence[j]

print(count)
print(' '.join([str(x) for x in gis]))
