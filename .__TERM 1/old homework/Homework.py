word = str(input('Give word ("_stop" to exit): '))
while word != '_stop':
    if len(word) > 3:
        if word[-1] == 'g' and word[-2] == 'n' and word[-3] == 'i':
            word += 'ly'
        elif word[-1] == 'e':
            word = word[:-1]
            word += 'ing'
        else:
            word += 'ing'
    print(word)
    word = str(input('Give word: '))


