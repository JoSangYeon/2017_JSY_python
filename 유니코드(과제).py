dic = {20171706: '조상연', 30818: '조상연', 20926: '조상연'}
for key in dic:
    print(key)
    print(dic.values())

dic['상연'] = 'whtkddus'
print(dic)

sett = [1,5,3]

print(sett)


g = {'Alpha': '알파','Beta': '배타', 'Gamma': '감마', 'Delta': '델타' }
print(g)

greek_alphabet = {
    'Alpha': u'\u0391',
    'Beta': u'\u0392',
    'Gamma': u'\u0393',
    'Delta': u'\u0394',
    'Epsilon': u'\u0395',
    'Zeta': u'\u0396',
    'Eta': u'\u0397',
    'Theta': u'\u0398',
    'Iota': u'\u0399',
    'Kappa': u'\u039A',
    'Lamda': u'\u039B',
    'Mu': u'\u039C',
    'Nu': u'\u039D',
    'Xi': u'\u039E',
    'Omicron': u'\u039F',
    'Pi': u'\u03A0',
    'Rho': u'\u03A1',
    'Sigma': u'\u03A3',
    'Tau': u'\u03A4',
    'Upsilon': u'\u03A5',
    'Phi': u'\u03A6',
    'Chi': u'\u03A7',
    'Psi': u'\u03A8',
    'Omega': u'\u03A9',
    'alpha': u'\u03B1',
    'beta': u'\u03B2',
    'gamma': u'\u03B3',
    'delta': u'\u03B4',
    'epsilon': u'\u03B5',
    'zeta': u'\u03B6',
    'eta': u'\u03B7',
    'theta': u'\u03B8',
    'iota': u'\u03B9',
    'kappa': u'\u03BA',
    'lamda': u'\u03BB',
    'mu': u'\u03BC',
    'nu': u'\u03BD',
    'xi': u'\u03BE',
    'omicron': u'\u03BF',
    'pi': u'\u03C0',
    'rho': u'\u03C1',
    'sigma': u'\u03C3',
    'tau': u'\u03C4',
    'upsilon': u'\u03C5',
    'phi': u'\u03C6',
    'chi': u'\u03C7',
    'psi': u'\u03C8',
    'omega': u'\u03C9',
}

print(greek_alphabet)
print(greek_alphabet.keys())
print(greek_alphabet.values())

string = input('영어로 쓰세요: ')
l = string.split()
print(l)
for i in ragne(10):
