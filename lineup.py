numb=int(input())
name=[]
for j in range(numb):
#     a=input()
#     if not(len(a.split())>1):
#         if a not in name:
#             name.append(a)
# print(len(name),name)
    order=[]
    for x in name:
        order.append(ord(x[0]))
    if sorted(order)==order:
        print("INCREASING")
    elif sorted(order,reverse=True)==order:
        print("DECREASING")
    else:
        print('NEITHER')
