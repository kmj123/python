a = 10
b = 3
print("더하기:",a+b)
print("빼기:",a-b)
print("곱하기:",a*b)
print("나누기: {:.2f}".format(a/b))
print("나머지:",a%b) #나머지 - a를 b로 나눴을때 나오는 값에서 몫: //, 나머지: %
print("몫:",a//b) #몫
print("제곱:",a**b) 

c = 10
d = 20

e = 30; f = 40
g,h = 10,20

# bool타입: True, False
bo1 = (100 > 10) #참 = True
print(bo1)

# 수학에서의 같다 =, 프로그래밍 같다 ==
bo2 = (100==10)
print(bo2)

bo3 = True; bo4 = False
num = 10            # 다른 타입인 경우 따로 쓰기
bo5 = True

str1 = "안녕하세요"
str2 = "10" #문자열
str3 = "10+40" #계산이 안됨, 문자열 그자체로 출력됨
print(str3)
print(10+40)
print("-"*50)

str4 = """\
1. 동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세

2. 남산 위에 저 소나무 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세

3. 가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세

4. 이 기상과 이 맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
"""

print(str4)