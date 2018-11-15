monthDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

while True:
    fullDate = str(input("Give me the date in dd/mm/yyyy: ")) 
    slashes = 0
    for a in fullDate:
        if a == '/':
            slashes += 1
    if slashes != 2:
        continue
    d, m, y = fullDate.split('/')
    if not d.isdigit():
        continue
    if not m.isdigit():
        continue
    if not y.isdigit():
        continue
    d = int(d)
    m = int(m)
    y = int(y)

    if d < 1 or d > 31:
        continue
    if m < 1 or m > 12:
        continue

    selectedMonth = monthDict[m-1]
    newDateString = 'The date is ' + selectedMonth + ' ' + str(d) + ', ' + str(y)
    print(newDateString)
    input()
