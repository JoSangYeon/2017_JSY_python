dic = {
    'A': u'\u0391',
    'B': u'\u0392',
    'G': u'\u0393',
    'D': u'\u0394',
    'E': u'\u0395',
    'Z': u'\u0396',
    'E': u'\u0397',
    'T': u'\u0398',
    'I': u'\u0399',
    'K': u'\u039A',
    'L': u'\u039B',
    'M': u'\u039C',
    'N': u'\u039D',
    'X': u'\u039E',
    'O': u'\u039F',
    'P': u'\u03A0',
    'R': u'\u03A1',
    'S': u'\u03A3',
    'T': u'\u03A4',
    'U': u'\u03A5',
    'P': u'\u03A6',
    'C': u'\u03A7',
    'P': u'\u03A8',
    'O': u'\u03A9',
    'a': u'\u03B1',
    'b': u'\u03B2',
    'g': u'\u03B3',
    'd': u'\u03B4',
    'e': u'\u03B5',
    'z': u'\u03B6',
    'e': u'\u03B7',
    't': u'\u03B8',
    'i': u'\u03B9',
    'k': u'\u03BA',
    'l': u'\u03BB',
    'm': u'\u03BC',
    'n': u'\u03BD',
    'x': u'\u03BE',
    'o': u'\u03BF',
    'p': u'\u03C0',
    'r': u'\u03C1',
    's': u'\u03C3',
    't': u'\u03C4',
    'u': u'\u03C5',
    'p': u'\u03C6',
    'c': u'\u03C7',
    'p': u'\u03C8',
    'o': u'\u03C9',
}

def converter():
    conv = input("변환할 문자를 입력하세요: : ")
    for i in range(len(conv)):
        if conv[i] in dic:
            print(dic[conv[i]],end = "")
        else:
            print(conv[i],end = "")
    print()

while(1):
    converter()
