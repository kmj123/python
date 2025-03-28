# # 숫자 2개를 입력받아, 사칙연산 결과값을 출력하시오. 
# # format() 함수 사용
# # 출력형태는 
# # 10 + 5 = 15
# # 10 - 5 = 5
# # 10 * 5 = 50
# # 10 / 5 = 2

a = int(input("1. 숫자를 입력하세요> "))
b = int(input("2. 숫자를 입력하세요> "))

str_print1 = "{} + {} = {}".format(a,b,a+b)
str_print2 = "{} - {} = {}".format(a,b,a-b)
str_print3 = "{} * {} = {}".format(a,b,a*b)
str_print4 = "{} / {} = {:.1f}".format(a,b,a/b)
print(str_print1)
print(str_print2)
print(str_print3)
print(str_print4)

#------------------------------------------------------------------
# 국어, 영어, 수학 점수를 입력받아 평균을 출력하시오
# 합계: 240
# 평균: 80

kor = int(input("국어점수를 입력하세요: "))
eng = int(input("영어점수를 입력하세요: "))
math = int(input("수학점수를 입력하세요: "))
total = kor+eng+math
avg = (kor+eng+math)/3

total_score = "합계: {}".format(total)
print(total_score)
total_avg = "평균: {:.2f}".format(avg)
print(total_avg)