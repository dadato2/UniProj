from os import system

class Human:
    backstory = ""
    insurances = {"Phone": 2, "Computer": 5, "Car": 10}
    def __init__(self, name, nationality, job):
        self.name = name
        self.nationality = nationality
        self.job = job

    def addBackstory(self, story):
        self.backstory = str(story)

    def givebackstory(self):
        print(self.name + " - " + self.backstory)

    def info(self):
        print("{}, the {} {} - {}".format(self.name, self.nationality,  self.job, self.backstory))

    def breakDown(self, gadget):
        self.insurances[gadget] -= 1

    def insuranceLeft(self, gadget):
        print(self.insurances[gadget])


human1 = Human("Joel", "Hungarian", "teacher")
human2 = Human("Richard", "French", "doctor")

human1.addBackstory("They went to a store as a kid and lost their mother.")
human2.addBackstory("They used to bully a kid at school.")
human1.info()
human2.info()

human1.breakDown("Phone")
human1.insuranceLeft("Phone")

print("helo".format())