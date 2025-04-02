# # # 문자열 # # #

# print('1234'.isdigit()) # 숫자인지 확인
# print('abcd'.isalpha()) # 알파벳인지 확인 - 한글 안됨
# print('abc123'.isalnu,) # 모두 숫자인지 확인 - abc, a1,123 모두 가나ㅡㅇ
# print('abc'.islower())  #모두 소문자인지 확인
# print('ABC'.isupper())  # 모두 대문자인지 확인


# a = "1,2,3,4"
# if a.isdigit(): # 숫자로 변환가능
#     print("숫자로 가능합니다.")
    
# my = int(input("숫자를 입력하세요>>"))  # 문자열 입력시 종료된다

# while True:
#     my_input = input("숫자를 입력하세요>>")
#     if my_input.isdigit():    # 프로그램이 다운되지 않는다!
#         my_input = int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력하셔야 합니다.")
    

# map(함수, 데이터값)
# score = ['100','99','90']
# # 함수
# def cal(x):
#     return int(x)*100

# s_list = list(map(int,score))
# print(s_list)


# sum = 0
# for s in score: 
#     sum= sum + int(s)   # 형변환 str -> int
# print("합계 : ",sum)



# txt = ","
# txt2 = txt.join("안녕하세요")   # txt에 있는 글자를 join 글자 사이사이에 넣어준다.
# print(txt2)


# 데이터베이스(DB) 는 리스트를 저장할 수 없음
# txt = "1,홍길동,100,100,100300,100.0,1"
# txt_list = txt.split(",")
# txt_list[1] = "유관순"
# print(txt_list)


# txt = "a,b,c,d,안녕,반가워"
# txt_list = txt.split(",")
# print(txt_list)     # ['a', 'b', 'c', 'd', '안녕', '반가워']


# txt = " 안녕하  세요  "
# print(txt.replace("","")) # 문자를 다른 문자로 치환


# txt2 = "파이썬 공부하기 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요"
# print(txt2.replace("파이썬", "자바"))

# txt3 = "----파----이썬----"
# print(txt3.strip("-"))  # 특정글자제거(중간은 제거 불가)
# print(txt3.replace("-","")) #replace를 이용하여 - 문자열을 공백으로 치환시켜서 문자열 없애기

# print(txt.strip())  # 앞, 뒤 공백만 제거 - rstrip(): 오른쪽 공백 제거, lstrip(): 왼쪽 공백 제거


# txt = "파이썬 공부하기 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요"
# print(txt.count("파이썬"))  # 문자열의 검색하려고 하는 글자 개수
# print(txt.count("요"))
# print(txt.find("공부"))     # 문자열이 몇 열에 있는지 찾아줌 : 있을땐 index 번호 출력
# print(txt.find("자바"))     # 없으면 -1 로 리턴


# t = "aaa.py"
# print(t.endswith("py")) # 있으면 True, 없으면 False


# # 대소문자 문자열

# txt ="abBBcDd" 
# print(txt.upper())      # 대문자로 출력
# print(txt.lower())      # 소문자로 출력
# print(txt.swapcase())   # 대문자는 소문자로, 소문자는 대문자로 출력
# print(txt.title())      # 단어 첫글자 대문자


# txt 출력

# txt = "안녕하세요"
# a_list = [1,2,3,4,5]

# print(a_list[1:3])  # 3의 앞에까지만 출력; 1,2열만 출력
# print(txt[1:3])     # 녕하 3의 앞에까지만 출력; 1,2열만 출력
# print(txt[2:])      # 2열부터 끝까지 출력

# print(txt*3)        # 글자를 횟수만큼 출력
# print("-"*50)
# print(len(txt))     # 글자 길이 출력

# print(txt[::-1])    # 글자 역순 출력


# # 문자열 index 번호 가짐
# print(txt[1])

# print(a_list[1])