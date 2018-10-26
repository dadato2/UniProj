


input('End of section, press enter to continue:')

listOfStrings = []
string = ""
while True:
    string = str(input("Give word(stop to stop): "))
    if string == "stop":
        break
    listOfStrings.append(string)

listWithX = []
listAlpha = []

for word in listOfStrings:
    if word[0] == 'x':
        listWithX.append(word)
    else:
        listAlpha.append(word)

print(*(sorted(listWithX)+sorted(listAlpha)))