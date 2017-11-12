cards=input()
if len(cards)<=50:
    cards=list(cards)
    c=cards.count('C')
    t=cards.count('T')
    g=cards.count('G')
    if c>0 and t>0 and g>0:
        if c<t and c<g:
            small=c
        elif t<g:
            small=t
        else:
            small=g
        total=c*c+t*t+g*g+7*small
        print(total)
    else:
        total=c*c+t*t+g*g
        print(total)
