while True:
    a = str(input("GIve me a string: "))
    codeCount = 0
    hicount = 0
    for char in range(0, len(a)):
        if a[char] == 'c':
            if a[char+1] == 'o':
                if a[char+3] == 'e':
                    codeCount += 1
        if a[char] == 'h':
            if a[char+1] == 'i':
                hicount+=1
    print("c o [X] e :" + str(codeCount) + " times;\nh i : " + str(hicount) + " times")

