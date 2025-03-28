# 1. 두 숫자를 입력받아, 합과 곱을 출력하시오.

a = int(input("1. 숫자를 입력하시오."))
b = int(input("2. 숫자를 입력하시오."))
a = int(a)
b = int(b)

print(a)
print(b)
print(a,b)

print(type(a))
print(type(b))

print(a+b)
print(a*b)
print("두 수 출력: ", a,b)

# # a,b라는 변수에 입력받아, a,b를 출력하고 a,b의 값을 교체해서 출력하시오.
c = a
a = b
b = c 
print("두 수 출력: ", a,b)

# a = 100             #int 타입
# st = "안녕"         #str 타입
# print("변수값: ", a)
# print("변수값: "+ a) #에러 - 다른타입을 +연산자를 사용할수없음
# print("변수값: ", st)
# print("변수값: "+ st)

a = 10
b = 5
print(a,"+",b,"=",a+b)

c = 100
d = 7
print(c,"*",d,"=",c*d)
print("%d * %d = %d" % (c,d,c*d))
print(c,"/",d,"=",c/d)
print("%d / %d = %07.2f" % (c,d,c/d))