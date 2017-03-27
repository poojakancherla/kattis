for i in range(15):
    s=[int(x) for x in input().split()]
    if s[0]==0 and s[1]==0 :
        break
    elif s[0]>s[1] and s[0]+s[1]!=13 :
        print('To the convention.')
    elif s[0]<s[1] and s[0]+s[1]!=13 :
        print('Left beehind.')
    elif s[0]+s[1]==13:
        print('Never speak again.')
    elif s[0]==s[1] and s[0]+s[1]!=13 :
        print('Undecided.')
