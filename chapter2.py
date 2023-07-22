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