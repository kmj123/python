a, b = 100, 200
c = 300; d = 400
e = 500
f = 600

# 관계 연ㄴ산자 - True, False
# print(a==b)
# print(a!=b)
# print(a>b, a<b, a>=b,a<=b)

# # tap 들여쓰기 shift tap 내어쓰기
# # 조건식
# a = int(input("숫자를 입력하세요."))
# if a<100: #True
#     print("입력한 값은 100보다 작은 수 입니다.")
# else:   #False
#     print("입력한 값은 100보다 큰 수 입니다.")

# # 양수, 음수 인지 확인 - 0양수로 하겠습니다.
# input_num = int(input("숫자를 입력하시오.>>"))
# if input_num>=0:
#     print("양수입니다.")
# else: 
#     print("음수입니다.")

# num -> 짝수인지, 홀수인지 구현 num % 2 == 0 (짝수), =1 (홀수)
num = int(input("숫자를 입력하시오>>"))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("음수입니다.")
    
if num%3 == 0:
    print("3의 배수입니다.")
else: 
    print("3의 배수가 아닙니다.")
    
if num%3 == 0 :
    print("3의 배수입니다.")
if num%3 != 0 :
    print("3의 배수가 아닙니다.")