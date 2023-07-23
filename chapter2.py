def test(t):
	print(x)
	t = 20
	print("In Function:", t)

# 전역변수
x = 10
test(x)
print("In Main:", x)
# print("In Main:", t)

def calculate(x,y):
	total = x+y # 새로운 값이 할당되어 함수 내부 total은 지역 변수가 됨
	print("In Function")
	print("a:", str(a), "b:", str(b), "a+b:", str(a+b), "total:", str(total))
	return total

a = 5 # a와 b는 전역변수
b = 7
total = 0 # 전역 변수 total

print("In Program -1")
print("a:", str(a), "b:", str(b), "a+b:", str(a+b))

sum = calculate(a,b)
print("After Calculation")
print("Total:", str(total), "Sum:", str(sum)) # 지역 변수는 전역 변수에 영향을 주지 않음

def exam_func():
	c = 10 # 먼저 선언하면 unboundlocalerror 안남
	print("Value:", c)
# 만약 x = 10 여기에 있으면 에러남

c = 20 # 어디에 위치하든 함수 안에서 print 다음에 나오면 에러남
exam_func()
print("Value:", c)


a = [1, 2, 3, 4, 5]

def swap_value(d,e):
	temp = d
	d = e
	e = temp
print(a)

def swap_offset(offset_d, offset_e):
    temp = a[offset_d]
    a[offset_d] = a[offset_e]
    a[offset_e] = temp
print(a)

def swap_referece(list, offset_d, offset_e):
    temp = list[offset_d]
    list[offset_d] = list[offset_e]
    list[offset_e] = temp
print(a)

d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print(d[:-15])

print('It\’s OK. "See you" #')


title = "TEAMLAB X Inflearn"

print(title.upper())
print(title.lower())
print(title.split(" "))

print(title.count("a")) # title 변수에 'a'가 몇 개 있는지 개수 반환
print(title.upper().count("a")) # title 변수를 대문자로 만든 후, 'a'가 몇 개 있는지 개수 반환

print(title.isdigit()) # title 변수의 문자열이 숫자인지 여부 반환
print(title.title())
print(title.startswith("a")) # title 변수가 'a' 로 시작하는지 여부 반환

title_2 ="12345"

print(title_2.isdigit())

print(title.find("Gachon"))

print(title.upper().find("Gachon"))

print("    Hello    ".strip())

print("A-B-C-D-E-F".split("-"))


# lab counting
f = open("asap_lyrics.txt", 'r')
asap_lyric = ""
while 1:
	line = f.readline()
	if not line:
		break
	asap_lyric = asap_lyric + line.strip() + "\n"
f.close()

n_of_tik = asap_lyric.lower().count("tik")
print("Number of a Word 'tik'", n_of_tik)


def test(t):
	t = 20 # 사라짐
	print("In function :", t)

x = 10
print("Before :", x) # 10
test(x) # 함수 호출
print("After :", x) # 10 - 함수 내부의 t는 새로운 주소값을 가짐