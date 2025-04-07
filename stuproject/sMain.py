# 1. sModule.py - class 2개
# 2. sMain.py
# - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄
from sModule import Student,Students
from sFunc import *
stuents = Students()


while True:
    # 메인화면
    choice = main_print()
    
    # 성적 입력
    if choice == 1:
        stu_input()
        
    # 성적 출력 
    elif choice == 2:
        stu_output()
