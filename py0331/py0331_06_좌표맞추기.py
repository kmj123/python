# x좌표: 1
# y좌표: 2
# 1,3 -> 문자로 인식
# str -> int타입으로 바꾸기

# num1 = int(input("X좌표: "))
# num2 = int(input("Y좌표: "))

# print((f"[X,Y 좌표: {num1},{num2}]"))

num = input("X,Y좌표 (0/0) : ")
n_list = num.split("@") # 뒷 문자의 타입으로 문자열을 끊어줌
print(f"[X,Y좌표 : {n_list} ]")