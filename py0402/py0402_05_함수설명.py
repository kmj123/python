def cal(*a, b=10):  # 가변매개변수, 키워드 매개변수 함께 사용 - 매개변수 키워드
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,b=100))



# # 키워드 매개변수 - 키워드 변수는 무조건 마지막에 있어야함.
# def cal(a, b=10):   # 키워드 변수는 반드시 뒤쪽에 있어야한다.
#     return a+b

# print(cal(1))

# # print() 함수는 매개변수가 가변매개변수임
# print(1,2,3,4,5)
# print(1,2)



# # 가변매개변수 사용
# def cal(*num):  # 전개 연산자 1,2,3,4,5
#     result = 0
#     for n in num:
#         result += n
#     return result

# print("2개 합계: ", cal(1,2))
# print("3개 합계: ", cal(10,20,30))
# print("4개 합계: ", cal(20,40,60,80))

# def cal(n1, n2):
#     return n1+n2
# def cal2(n1,n2,n3):
#     return n1+n2+n3

# n1 = 10
# n2 = 20
# n3 = 30

# result = cal(n1,n2)
# print(result)
# print(result)

# result2 = cal2(n1,n2,n3)
# print(result)


# # global 변수 : 전역변수
# def func1():
#     global a    # 전역변수 호출
#     a = 20
#     # a = 20  # 지역변수이기에 함수를 벗어나면 사라짐.

# a = 10
# print("a : ",a)
# func1()
# print("a: ",a)



# # 국어점수 변경함수 선언
# def cal(ss):
#     ss['kor'] = int(input("수정 할 국어점수 입력: "))
#     ss['total'] = ss['kor']+ss['eng']+ss['math']
#     ss['avg'] = ss['total']/3

# print("[학생성적 수정]")
# s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

# # 국어점수 변경 함수
# cal(s)  # return kor, kor = cal(kor) 선언해줘야지 변경된 국어점수가 입력됨
# print("수정된 국어점수: ",s['kor'])


# # 매개변수로 일반변수 전달 - 리턴으로 값을 돌려줘서 입력을 시켜야함.
# # 국어점수 변경함수 선언
# def cal(kor):
#     kor = int(input("수정 할 국어점수 입력: "))
#     return kor  # return kor, kor = cal(kor) 선언해줘야지 변경된 국어점수가 입력됨

# print("[학생성적 수정]")
# kor = 100
# eng = 100
# math = 100

# # 국어점수 변경 함수
# kor = cal(kor)  # return kor, kor = cal(kor) 선언해줘야지 변경된 국어점수가 입력됨
# print("수정된 국어점수: ",kor)



# # 함수 호출 전 호출 후 데이터값 변화
# def cal(b_list):
#     b_list[0] = 100
#     b_list[1] = 200
    
# a_list = [10,20]    #리스트타입 변수 : 주소값
# a_list[0] = 10
# a_list[1] = 20

# print("함수 호출 전 a_list: ",a_list[0],a_list[1])

# cal(a_list) # b_list = a_list
# print("함수호출 후 a_list: ",a_list[0],a_list[1])


# # 함수선언
# def cal(a,b):
#     a = 100 # 지역변수 - 함수 내 일반 변수는 함수를 벗어나면 사라짐 -bool, int ,float
#     b = 200

# #--------------------------------
# # 함수 밖
# a = 10  # 전역변수
# b = 20  
# print("함수호출 전 a,b : ",a,b) #a=10, b=20

# # 함수 호출
# cal(a,b)
# print("함수호출 후 a,b :", a,b) #a=?, b=?


# # 이름, 국어, 영어, 수학 점수를 입력받아, 합계, 평균을 출력하시오.
# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ]
# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")

# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice = int(input("원하는 번호를 입력하세요>>"))
# if choice == 2:
#     stu_print() # 함수 호출
    

# #함수 선언
# def cal(kor,eng,math):
#     return kor+eng+math, (kor+eng+math)/3

# no = 1
# name = input("이름을 입력하세요>>")
# kor = int(input("국어점수를 입력하세요>>"))
# eng = int(input("영어점수를 입력하세요>>"))
# math = int(input("수학점수를 입력하세요>>"))

# total,avg = cal(kor,eng,math)


# 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오
# 가로*세로, 가로길이*2+세로길이*2

# 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.
# 함수를 사용할 것
# def cal(num1, num2):
#     result1 = num1*num2
#     result2 = (num1*2)+(num2*2)
#     return result1, result2


# # 가로, 세로 입력
# num1 = int(input("가로길이: "))
# num2 = int(input("세로길이: "))

# result1,result2 = cal(num1, num2)
# print("넓이: ",result1, "길이: ",result2)


# # cal 함수선언 하시오.
# def cal(n_llist):
#     sum = 0
#     for n in n_list:
#         if n%2 == 0: sum += n
#     return sum


# # 입력을 5개를 받아, 짝수만 모두 더한 값을 출력하시오.
# n_list = [0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자입력"))
# result = cal(n_list)
# print("짝수의 합: ", result)


# 함수를 사용해서 두 수를 입력받아
# 10~ 20 입력받으면 10+11+12+,,,+20 출력하시오.

# def add(n1, n2):
#     sum = 0
#     for i in range(n1, n2+1):
#         sum += i
#     print("합계: ",sum)
    
# n1 = int(input('숫자를 입력하세요>>'))
# n2 = int(input("숫자를 입력하세요>>"))

# # 10~20 입력ㅂ큰 수를 먼저 넣어도 10,2 -> 2,10
# def add(n1, n2):
#     if n1>n2 :n1,n2 = n2,n1
#     sum = 0
#     for i in range(n1, n2+1):
#         sum += 1
#         print("합계: ",sum)

# add() 결과값 출력

# um1, num2, num3 값을 입력받아, 합계, 평균을 구하시오
# 1. 중복코드가 있을때
# 2. 소스가 너무 복잡할때
#. 먼저 프로그램을 구현해놓고, 중복되고 있는지 확인 후 함수를 사용

# # 함수선언
# def add(kor,eng,math):
#     return kor+eng+math

# kor = int(input('점수를 입력하세요>>'))
# eng = int(input('점수를 입력하세요>>'))
# math = int(input('점수를 입력하세요>>'))
# total = kor+eng+math
# avg = total/3

# print(kor,eng,math,total,avg)