while True:
    a = str(input("GIve me a string: "))
    codeCount = 0
    for char in range(0, len(a)):
        if a[char] == 'c':
            if a[char+1] == 'o':
                if a[char+3] == 'e':
                    codeCount += 1
    print(codeCount)
