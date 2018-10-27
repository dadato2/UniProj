myDict = {'Name': ['Peter', 'Pan']}
newl = myDict["Name"]
print(newl[1])

input('End of section, press enter to continue:')

inter = ('', 'f', '', 'fff', 'ff')
inerer = []
for i in inter:
    if i:
        inerer.append(i)
print(inerer)

input('End of section, press enter to continue:')

ui = str(input("Name: "))
print(' '.join(ui) + " ? ? ?")

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