def skalia(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        b_1 = 1
        b_2 = 2
        for i in range( int(num-2)):
            result = int(b_1) + int(b_2)
            b_1 = b_2
            b_2 = result
        return result

print("you want to run it Yes/No")
answer = input()
while answer == "Yes" :
    print("give a number >0")
    num = input()
    while int(num) <= 0:
        print("give a number >0")
        num = input()
    print(skalia( int(num)))
    print("you want to run again; Yes/No")
    answer = input()












