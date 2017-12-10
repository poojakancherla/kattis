n = int(input())

costs = []
for i in range(n):
    costs.append(int(input()))

costs = sorted(costs, reverse = True)

i = 0
value = 0
while(i < n):
    if n - i >= 3:
        value += costs[i] + costs[i+1]
        i = i + 3
    else:
        value += sum(costs[i:n])
        i = n
print(value)
