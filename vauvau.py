for i in range(2,999):
    dog1, dog1_peace, dog2, dog2_peace=map(int, input().split())
    postman, milkman,garbageman=map(int, input().split())
    if dog1>=postman and dog2>=postman:
        print('both')
    elif dog1>=postman or dog2>=postman:
        print('one')
    else:
        print('none')
    if dog1>=milkman and dog2>=milkman:
        print('both')
    elif dog1>=milkman or dog2>=milkman:
        print('one')
    else:
        print('none')
    if dog1>=garbageman and dog2>=garbageman:
        print('both')
    elif dog1>=garbageman or dog2>=garbageman:
        print('one')
    else:
        print('none')
