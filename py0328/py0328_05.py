# 3,5,7,9 홀수단만 출력
#(2, 9+1,1) 도 가능은 하나 비추천

# 시작단과 끝나는 단을 입력받아, 출력하시오.
# 2, 6 -> 2~6단 까지 출력
num1 = int(input("숫자를 입력하세요>>"))
num2 = int(input("숫자를 입력하세요>>"))

if num1>num2:
    num1,num2 = num2,num1

for i in range(num1, num2+1):
    print("[{} 단]".format(i))
    for j in range(1,9+1):
        print("{}X{}={}".format(i,j,i*j))
    print()


# 구구단 출력 (이중 for문)
# for i in range(2, 9+1):
#     # if
#     if i%2 == 1:
#         print("[{}단]".format(i))
#         for j in range(1, 9+1):
#             print("{} X {} = {}".format(i,j,i*j))
#         print()


# # 두 수를 입력받아, 두수 사이의 합계를 구하시오
# # 예: 1,7 을 입력받은 경우 -> 1,2,3,4,5,6,7 의 합을 출력하기

# # 10,1 을 넣었을때 자동으로 1,10 으로 계산해주기

# num1 = int(input("숫자를 입력하세요>>"))
# num2 = int(input("숫자를 입력하세요>>"))

# # sum = 0

# # for i in range(num1,num2+1):
# #     sum = sum+i
# #     print("i: {}, sum: {}".format(i,sum))

# # print("{}에서 {}까지의 합계: {}".format(num1,num2,i))

# # if문 비교 num1, num2에서 num2가 더 큰지 확인
# if num1 > num2: 
#     t = num1
#     num1 = num2
#     num2 = t
#     # num1, num2 = num2, num1 / 파이썬에서만 가능한 방법

# sum = 0

# for i in range(num1,num2+1):
#     sum = sum+i
#     print("i: {}, sum: {}".format(i,sum))

# print("{}에서 {}까지의 합계:
# {}".format(num1,num2,i))

