a = [1, 2, 13, 5, 6, 1, 1, 1, 1, 3, 1, 13, 999999]
sum = 0

for i in range(len(a)):
    if len(a) == 0:
        break
    if a[i] == 13:
        continue
    if a[i-1] == 13:
        continue
    if i < len(a)-1:
        if a[i+1] == 13:
            continue
    sum += a[i]
print(sum)
