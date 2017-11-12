def checkEqual(new):
    return new[1:] == new[:-1]
seq=input().split()
seq=[int(x) for x in seq]
seq_num=seq[0]
del seq[0]
lst=[]
lst.append(seq)
def difference(seq):
    new=[]
    new = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    lst.append(new)
    seq=new
    if checkEqual(seq)!=True:
        difference(seq)
difference(seq)
v=0
for x in lst:
    v+=x[-1]

print(len(lst)-1, v)
