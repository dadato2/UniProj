# constants
action = ''
error = 'Command not available. You can type "help" for example options.'

# Health and vitals
thirst = 10   # max 10
hunger = 10   # max 10
maxHealth = 10
health = 10
attack = 4

# Resources
water = 2
food = 1


# Start of story.
print('You have been travelling for a long time. You have two water bottles and a sandwich.'
      '\nYou can not see the end of the road. '
      '\nYou are thirsty and hungry. what do you do')

while True:
    action = str(input('What do you do: '))

    if action == "walk" or action =="run":
        print("You are hungry and thirsty. Walking seems difficult at the moment.")
        print("Available resources: ")
        print("water: ", water)
        print("food: ", food)

    elif action == 'drink' or action == 'drink water':
        print("You drink the water.")
        break

    elif action == 'eat' or action == 'eat sandwich' or action == 'eat food':
        print("You eat the food.")
        break

    elif action == 'rest' or action == 'sit' or action == 'sleep':
        print('You can\'t rest now. You have a long trip ahead of you.')
