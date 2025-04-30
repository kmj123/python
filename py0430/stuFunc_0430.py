# 상단메뉴
def stu_main_top():
    print(" [학생 성적 프로그램] ")
    print("-"*45)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("4. 학생성적정렬")
    print("4. 학생성적검색")
    print("0. 프로그램종료")
    print("-"*45)
    choice = int(input("실행할 프로그램 번호를 입력하세요>>"))
    return choice

    