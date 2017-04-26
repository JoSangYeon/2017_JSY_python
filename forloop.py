for i in [9,8,7,6,5,4,3,2,1]:
    print("Hi")
    print("The number is ",i)
print("done")
# for loop의 특징은 끝나는 조건이 있는것입니다.
for x in range(10):
    print(x)
for y in range(0,10,2):
    print(y)
for z in range (10,0,-2):
    print(z)
animal = ["dog","wolf","cat"]
for a in animal:
    print(a)
for b in range(6):
    print('b=',b)
    print("Hello","how")
    if b == 3:
        continue
    print("are you today?")
for c in range(6):
    print('c=',c)
    print("Hello","how")
    if i == c:
        break
    print("are you today?")
