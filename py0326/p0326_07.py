# a = 100
# b = 50
# # b = 10, a= 5 값을 변경하면 될까요?
# print(a)
# print(b)

# a = b
# b = a

# print(a) # 100
# print(b) # 50

# # 두변수의 값을 교체하려면, 추가적인 변수 c를 하나에 두고 값을 보관해서 견제
# c = a
# a = b
# b = c

# a,b = b,a #파이썬 a, b의 변수값 교체 방법

# 입력 : input
# 출력 : print

# print(input("숫자를 입력하세요."))

# 변수() 있으면 함수 - 어떤 기능구현을 말함

# 입력 - 무조건, 문자열(str) 타입
# 타입 변경 - 정수 : int(), 실수 : float(), 문자열 : str()
a = input("1. 숫자를 입력하세요")
b = input("2. 숫자를 입력하세요")
a = float(a) # str -> int, float
b = float(b) # str -> int, float
print(a)
print(b)
print(a,b)
print(type(a)) # str - 문자열
print(type(b))
print(a+b) #100, 500, 600 -> 100500
