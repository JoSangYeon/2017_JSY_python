class KMU_Stu:
    name = "국민대학교 학생 Class"
    def __init__(self):
        self.name = "무명씨(이름없음)"
        self.id = 0
    def __str__(self):
        return self.name + ":" + str(self.id)
    def printName():
        print(AAA.name)

class SW_Stu(KMU_Stu):
    name = "소프트웨어학부 학생"
    def __init__(self):
        super(SW_Stu, self).__init__()
        pass

a = SW_Stu()
a.name = "최호경"
#a.id = 20171717
print(str(a))
