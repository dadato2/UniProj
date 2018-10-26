import random
print('''

quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \\
        :##.       ==             .###.       `.      `.    `\\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
_________ .__          .__       _________                ________________ 
\_   ___ \|  |_________|__| _____\_   ___ \  _______  ___/  _____/   __   \\
/    \  \/|  |  \_  __ \  |/  ___/    \  \/ /  _ \  \/  /   __  \\\\____    /
\     \___|   Y  \  | \/  |\___ \\\\     \___(  <_> >    <\  |__\  \  /    / 
 \______  /___|  /__|  |__/____  >\______  /\____/__/\_ \\\\_____  / /____/  
        \/     \/              \/        \/            \/      \/          
''')

for i in range(1, 10):
    for j in range(0, i):
        print("*", end=" ")
    print()


newList = []
string = ''
count = 0

while True:
    string = str(input())
    if string == 'stop':
        break
    newList.append(string)

for i in newList:
    if len(i) > 2:
        print(i)
        count +=1
print(count)

input()

myList = ['dagger', 'axe', 'sword', 'shield', 'sausage']
print(myList[random.randrange(0, len(myList))])
print(myList[0])
tempIt = myList[0]
myList[0] = myList[1]
myList[1] = tempIt
print(myList[0])
myList.append('randomLOL')
print(myList[len(myList)-1])
print(myList)
myList.pop(0)
print(myList)
myList.insert(0, 'baguette')
print(myList)









newstr = ""
while True:
    stringg = str(input("GetMe: "))

    if stringg == 'Python':
        for i in range(0, len(stringg)):
            if stringg[i] != 't':
                print(stringg[i], end='')
    print()

    if stringg == "stop":
        break



i = 0

for i in range(100):
    if (i-1) %25 == 0:
        print()
    print(i, end=" ")


gameOn = False
count = 0
end = random.randrange(100, 200)

print("")

while not gameOn:
    count += 1
    if (count - 1) % 25 == 0:
        print()
    if count == end:
        break
    if count % 2 == 0:
        continue
    if count / 10 == 0:
        print('00', count, end=' ')
    else:
        print(count, end=' ')


