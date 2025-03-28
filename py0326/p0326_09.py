# 이름, 국어, 영어, 수학 입력 받아 합계, 평균을 출력하시오.
# 이름: 홍길동
# 합계: 300
# 평균: 100.0 소수점은 한자리까지 출력하시오

# name = input("이름을 입력하세요 >>")
# kor = int(input("국어점수를 입력하세요 >>"))
# eng = int(input("영어점수를 입력하세요 >>"))
# math = int(input("수학점수를 입력하세요 >>"))
# sci = int(input("과학점수를 입력하세요 >>"))
# total = kor+eng+math+sci
# avg = (kor+eng+math+sci)/4

# print("이름: ", name)
# print("국어: ", kor)
# print("영어: ", eng)
# print("수학: ", math)
# print("과학: ", sci)
# print("합계: ", total) #kor+eng+math+sci 이렇게 넣어도 상관없음
# print("평균: %.1f" % avg) #kor+eng+math+sci 이렇게 넣을 경우 결과가 잘 안나올수 있음

#print시 \n : 엔터키, \t: tab키
#print("안녕하세요.\n 반갑습니다.\t 저는 홍길동이라고 합니다.")

# format(), f함수
#format() 문자형태 함수
a = 10
b = 3
print("%d / %d = %.2f" % (a,b,a/b))

str_print = "{} / {} = {:.2f}".format(a,b,a/b)

# f함수 = format()
str_print2 = f"{a} / {b} = {(a/b):.2f}"

print(str_print)
print(str_print2)