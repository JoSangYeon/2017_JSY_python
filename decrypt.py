key = int(input("복호화에 사용할 키를 입력하세요. : "))

encrypted = input("암호화된 문자나 코드를 입력하세요 : ")

print("원래의 문자는 ", end="")

for i in range(len(encrypted)):

    print(chr(ord(encrypted[i]) ^ key), end="")

print(" 입니다.")
