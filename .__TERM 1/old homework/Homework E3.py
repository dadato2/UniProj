a = [1, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5]
b = [ ]
b.append(a[0])
for i in range(len(a)):
    if i > 0:
        if a[i] != a[i-1]:
            b.append(a[i])
print(a)
print(b)
