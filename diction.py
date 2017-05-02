dic = {"20171721":"허진우","20171724":"황교민","20171710":"최근표"}
print(dic)
n = input("사전을 찾으려면 1, 사전에 추가하려면 2를 입력하세요 : ")
if n == "1":
	find = input("키값을 입력하세요 : ")
	print(dic[find])
if n == "2":
	new = input("추가할 키값을 입력하세요 : ")
	dic.update(new)


