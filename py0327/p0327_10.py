# 1-100 까지의 랜덤숫자를 생성해서 정답을 맞추는 프로그램 구현
#---------------------------------------------
# 도전 횟수: 5번
# 도전 번호: [1,2,3,4,5]
# 랜덤 번호: 5

# 1. 랜덤 숫자 생성
# 2.num list 생성
# 3. n 변수 생성
# 4. 10번 for문 생성
# 5.num list에 저장
# 6.정답 비교
# 7.데이터 출력

import random
ran_num = random.randint(1,100)
num = []
n = 0

for n in range(1,11):
    in_num = int(input("숫자를 입력하세요>"))
    num.append(in_num) 
    if in_num == ran_num:
        print("정답입니다. 랜덤 숫자: {}".format(ran_num))
        break
    elif ran_num > in_num:
        print("더 큰수를 입력하세요. 입력한 숫자: {}".format(in_num))
    else:
        print("더 작은 수를 입력하세요. 입력한 숫자: {}".format(in_num))

print("도전횟수: {}".format(n))
print("도전번호: {}".format(num))
print("랜덤번호: {}".format(ran_num))




