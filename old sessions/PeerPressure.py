inv =["apples", "rasist jokes", "an actual weapon", "ligma"]

listYes = ("yes", "yep","ya","noice","yas","yaas","yaaas","yaaaas","yaaaaas","correct", "yee", "ye", "yuhuh", "y", "ok", "okey dokey","okie dokie","positive")
listNo = ("no","nope","n","nuhuh","newp","negative","nein","nicht","never")
listCheckINv = ("check inv", "inv","check inventory","inventory")

gameOver = False
ui = ""

while gameOver == 0:
    ui = input("There is a chest! Do you want to open it?: ")
    if ui in listYes:
        print("It is actually very locked atm.")
        print("You have: ", inv)
        while True:
            ui = str(input("Do you want to use an item to open?"))
            if ui in listYes :
                while True:
                    ui = input("WHat ITeM?!?!?: ")
                    if ui in inv and ui != "ligma":
                        print("It WOrkED!!? You GotTed a 'not balls'")
                        inv.append("not balls")
                    elif ui == "ligma":
                        print("It WOrkED!!? You GotTed a ActUAL!!! 'balls'")
                        inv.append("balls")
                    break
                break

            elif ui in listNo:
                print("Why NOt??!?")
            else:
                print("What??!")
    elif ui in listNo:
        print("Why NOt??!?")
    else:
        print("What??")
