import random

cand = ["문재인","홍준표","안철수","유시민","심상정"]
people = ["황교민","최근표","조상연","한창희","이원형","장우석","장민혁","허진우"]

for i in range(len(people)+1):
    electer = random.randint(0,4)
    chooser = random.randint(0,len(people)-1)
    print("%s님이 뽑을 후보는 %s 입니다." %(people[chooser],cand[electer]))
