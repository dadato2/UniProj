import os
import time

'''
This is a copyrighted program. To use give author 10000000$

I have also committed once and i need to check if it works
'''

pu =5
print(pu)
print(not pu)

pupu = int(input("Numer: "))
if pupu<=100:
    print('It\'s too small')
elif pupu < 1000:
    print('Perfect')
else:
    print('Too big')

if pupu%2== 0:
    print("Number is even.")
else:
    print('Number is odd.')



input('\n\nEND OF CYCLE PRESS ENTER')
os.system('cls')


name = input("Name: ")
age = int(input("Age: "))

if(age<18):
    print('\nSorry, %s, but you are not old enough to drink. You need to be at lest 18.' %(name))
else:
    print('\nWow, %s, you are so old! %d is like a million years old, sure, you can drink.' % (name, age))

input('\n\nEND OF CYCLE PRESS ENTER')
os.system('cls')

price = int(input('Price: '))
tax = int(input('Tax (%): '))

newprice = price+ (price*tax)/100

print(newprice, '$')

input('\n\nEND OF CYCLE PRESS ENTER')
os.system('cls')

t = 0
while(3<4):
    print(int(t/60), ':', t%60)
    t += 1
    time.sleep(1)
    os.system('cls')