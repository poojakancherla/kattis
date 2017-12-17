total = {}
nums = [2, 7, 11, 15]
target = 9

for x in nums:
    if x in total:
        print(x, target-x)
    else:
        total[target-x] = 1
