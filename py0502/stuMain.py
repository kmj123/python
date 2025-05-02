from stuConn import *
# db 연결
conn = connections()
cursor = conn.cursor()

# 학생성적프로그램 구현
while True:
    print("[ 학생성적프로그램 ]")
    print("-"*45)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적검색")
    print("0. 프로그램 종료")
    print("-"*45)
    choice = int(input("원하는 번호를 입력하세요>>"))
    