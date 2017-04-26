from urllib.request import urlopen
#함수 호출법
f = urlopen("https://www.python.org/")
print(f.headers)
html = f.read()
print(html)
