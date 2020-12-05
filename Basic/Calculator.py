replay = "yes"
while replay == 'yes':
    print('Simple calculator')
    a = int(input("First Number = "))
    b = int(input("Second Number = "))
    print("press number to calculate ")
    print("1 = add")
    print("2 = substract")
    print("3 = multiply")
    print("4 = devide")
    calculate = input("what you want to do ?  ")

    if calculate == "1":
        print("Output=", a + b)
    elif calculate == "2":
        print("Output=", a - b)
    elif calculate == "3":
        print("Output=", a * b)
    elif calculate == "4":
        print("Output=", a / b)

    replay = input("Again (yes/no) = ")
    if replay == "no":
        break
    else :
        print("wrong keyword try again")
        replay = input("yes/no = ")
