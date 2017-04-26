key = int(input("암호화에 사용할 키를 입력하세요. : "))

original = input("암호화할 문자를 입력하세요. : ")

print("암호화된 문자는 ", end="")

for i in range(len(original)):

    print(chr(ord(original[i]) ^ key), end="")

print(" 입니다.")
