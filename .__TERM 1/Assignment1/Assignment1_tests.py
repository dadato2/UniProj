import sys
import time

def newprint(a):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
newprint("You have been surrounded by a pack of friendly-looking wolves.\nYou know, however that if you make the wrong move, they" +
         " will attack you without thinking!")