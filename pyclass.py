import random

genderlist = ["male","female"]
scorelist = ["A","B","C","D","E","F"]

class student:  # class ~ str, int
    studentname = "name"
    studentID = random.randint(1,10000)
    gender = genderlist[random.randint(0,1)]
    score = 0

    def dialogue1(self):
        print("Hello!")
    def studing(self):
        i = 0
        print("Studing.....")
        score = scorelist[i]
        i = i + 1
