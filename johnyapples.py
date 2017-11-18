apples, sack = map(int, input().split())



def total(apples, sack):
    left = apples - sack
    curr_dist = sack - 1
    rest_dist = curr_dist + left



while apples>=0:
    
    total(apples, sack)
    apples = left
    break

print(rest_dist)
