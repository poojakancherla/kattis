a = [368, 6748, 83645, 84736, 46363, 8647]
b = [67, 75, 6, 75, 76]
diff = []
if len(a) <= len(b):
    for i in range(len(a)):
        diff.append(a[i] - b[i])
else:
    for i in range(len(b)):
        diff.append(a[i] - b[i])


print(diff)
