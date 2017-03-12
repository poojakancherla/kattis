x=input()
y=input()
if x[-1]=='h' and y[-1]=='h':
    if len(x)<len(y):
        print('no')
    elif len(y)<=len(x):
        print('go')
