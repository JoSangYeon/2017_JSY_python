# This is the shitest python3 module
# Please do not use it

class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        msg = "(" + str(self.x) + ", " + str(self.y) + ")"
        return msg
    def __add__(self,other):
        return vec(self.x + other.x, self.y + other.y)

#vec class test

p = vec(3,4)
q = vec(-1,2)
r = p+q
print(p)
print(q)
print(r)

# 침ㄴㄴ ㅍㄷㅊ:
#     ㅇㄷㄹ __ㅑㅜ샤__(ㄴ딜, ㅌ, ㅛ)
#     ㄴ딜.ㅌ = ㅌ
#     ㄴ딜.ㅛ = ㅛ
#     ㅇㄷㄹ __ㄴㅅㄱ__(ㄴ딜):
#         늫 = "(" + ㄴㅅㄱ(ㄴ딜.ㅌ + ", " + ㄴㅅㄱ(ㄴ딜.ㅛ) + ")"
#         ㄱㄷ셔구 늫
#     ㅇㄷㄹ __ㅁㅇㅇ__(ㄴ딜,새독):
#     ㄱㄷ셔구 ㅍㄷㅊ(ㄴ딜.ㅌ + 새독.ㅌ, ㄴ딜.ㅛ + 새독.ㅛ)
