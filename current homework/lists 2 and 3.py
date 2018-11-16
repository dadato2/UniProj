string = str(input("give list of numbers, separated my a space: "))
list1 = list(map(int, string.split()))
for item in list1:
    if item % 2 == 0:
        list1.remove(item)
print(list1)
