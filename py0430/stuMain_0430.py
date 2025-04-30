### 학생성적 프로그램
import stuFunc_0430 as stu  # 함수파일
from stuFunc_0430 import *  # 함수파일 연결

students = []
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
count = 1


while True: 
    # 상단메뉴
    choice = stu_main_top()
    
    # 1. 학생 성적 입력
    if choice == 1:
        no = count
        name = input("학생이름을 입력하세요>>")

        while True: 
            kor = int(input("국어성적을 입력하세요>>"))  
            if 0<= kor <= 100: 
                break
            else : 
                print("0~100까지의 숫자를 입력하세요") 

        while True:  
            eng = int(input("영어성적을 입력하세요>>"))  
            if 0<= eng <= 100: 
                break
            else:
                print("0~100까지의 숫자를 입력하세요") 
                    
        while True:
            math = int(input("수학성적을 입력하세요>>"))  
            if 0<= math <= 100: 
                break
            else: 
                print("0~100까지의 숫자를 입력하세요") 

        total = kor+eng+math
        avg = total/3
        rank = 0
        count += 1

        students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
        print(f"{no}번 학생이 등록되었습니다.")
            
    
    # 2. 학생성적 출력
    elif choice == 2:
        print(" [학생 성적 출력] ")
        print("-"*45)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))

        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        
        
    # 3. 학생성적 수정
    elif choice == 3:
        name = input("수정할 학생 이름을 입력하세요>>")
        temp = 0    # 찾지못한경우
        
        for s in students:
            if s['name'] == name:
                temp = 1
                print(f"{name}번 학생을 찾았습니다.")
                print("-"*50)
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 종료")
                choice = int(input("수정할 과목의 번호를 선택하세요>>"))
                
                sub_list = ['','kor','eng','math']
                
                if choice == 1:
                    pre_score = s['kor']
                    print(f"현재 {title[choice+1]}점수: {pre_score}")
                    s['kor'] = int(input(f"변경 할 {title[choice+1]} 점수를 입력해주세요>>"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{no}번 학생의 점수가 {pre_score} 에서 {s[sub_list[choice]]}로 변경되었습니다.")
                
                elif choice == 2:
                    pre_score = s['eng']
                    print(f"현재 {title[choice+1]} 점수: {pre_score}")
                    s['eng'] = int(input(f"변경 할 {title[choice+1]} 점수를 입력해주세요>> "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{no}번 학생의 점수가 {pre_score} 에서 {s[sub_list[choice]]}로 변경되었습니다.")
                
                elif choice == 3:
                    pre_score = s['math']
                    print(f"현재 {title[choice+1]} 점수: {pre_score}")
                    s['math'] = int(input(f"변경 할 {title[choice+1]} 점수를 입력해주세요>> "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{no}번 학생의 점수가 {pre_score} 에서 {s[sub_list[choice]]}로 변경되었습니다.")

            
            if temp == 0:
                print(f"{name}학생이 없습니다 다시입력해주세요!")
    
    # 4. 학생성적 삭제
    elif choice == 4:
        name = input("성적을 삭제할 학생의 이름을 입력해주세요>>")
        temp = 0
        for i,s in enumerate(students):
            if s['name'] == name:
                temp = 1
                print(f"{no}번 {name}학생을 찾았습니다. ")
                answer = input("학생의 성적을 삭제할까요? 삭제후 복구 불가능 ")
                if answer == "y" : del students [i]
                print(f"{name} 학생을 삭제했습니다.")
                print()
                break
            
            if temp == 0:
                print(f"{name} 학생을 찾지 못했습니다. 다시입력해주세요")
                print()
    
    elif choice == 0:
        break