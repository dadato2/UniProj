a = input("Give me degrees in C or F: ")
mes = a[-1]
temp = float(a[:-1])
if mes == 'c' or mes == 'C':
    temp = round(9.0/5.0 * temp + 32, 2)
    mes = 'F'
elif mes == 'f' or mes == 'F':
    temp = round((temp-32) * 5.0/9.0, 2)
    mes = 'C'
print("This equals " + str(temp) + mes)
