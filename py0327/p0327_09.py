# import random

# 0보다 같거나 크코, 1 미만인 랜덤 실수 값을 뽑아서 전달해줌.
# 0 <= x < 1 = 0.12456574
# print(random.random()) # 실수값 출력

#print(random.randint(1,100)) #정수값 출력 0-99

# 랜덤 숫자를 맞추는 프로그램
# ran_num = random.randint(1,5)
# in_num = int(input("랜덤 숫자 맞추기!! 1-5까지의 숫자 1개를 입력하세요>>"))

# if ran_num == in_num:
#     print("정답입니다! \t랜덤 숫자 {}\t내가 입력한 숫자 {}".format(ran_num, in_num))
# else:
#     print("틀렸습니다... \t랜덤 숫자: {} \t내가 입력한 숫자 {}".format(ran_num, in_num))




# 1-100까지의 숫자 10개를 입력 받음

import random
num = []
# for 반복문
for n in range(1, 11): #1,2,3,4,5,6,7,8,9
    print(n)
    
# 1- 100 랜덤숫자 1개 생성    
ran_num = random.randint(1,100)
n = 0 # 몇번 시도햇는지 저장하기 위함

for n in range(1,11):
    in_num = int(input("숫자를 입력하세요.>>"))
    num.append(in_num) #num list타입에 데이터를 추가
    if ran_num == in_num:
        print("정답입니다 랜덤숫자:{}".format(ran_num))
        break
    elif ran_num>in_num:
        print("더 큰수를 입력하셔야 합니다. 입력한 숫자: {}".format(in_num))
    else:
        print("더 작은 수를 입력하세요. 입력숫자:{}".format(in_num))
        
print("도전횟수 : {}".format(n))
print("입력된 숫자 : {}".format(num))
print("랜덤 숫자: {}".format(ran_num))