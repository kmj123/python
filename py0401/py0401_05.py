students = [
    [1,'홍길동',100,100,100,300,100.0,1],
    [2,'유관순',100,100,99,299,99.67,2],
    [3,'이순신',100,100,99,299,99.67,2]
]

count = 4  # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# 무한반복
while True: 
    # 화면출력
    print(" "*30)
    print(""*5,end="")
    print("[  학생 성적 프로그램  ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("7. 등수처리")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>>"))
    
    if choice == 1:
        no = count
        name = input("학생이름을 입력하세요>>")
        kor = int(input("국어성적 입력: "))
        eng = int(input("영어성적 입력: "))
        math = int(input("수학성적 입력: "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        count += 1
        students.append([no,name,kor,eng,math,total,avg,rank])
        print(f"{name}이 등록되었습니다.")
        print()

    elif choice == 2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))  # 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수 를 분할시킴
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))  # 나뉘어진 # 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수 에 값을 넣어준다
    
    elif choice == 3:
        print("[학생성적 수정]")
        name = input("수정할 학생의 이름을 입력해주세요>>")
        temp = 0
        
        for i,s in enumerate(students):
            if name in s:
        # 수정할 학생이 있는 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print("[수정하려는 과목 선택]")
                print("-"*45)
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                print("-"*45)
                print(input("수정할 번호를 선택해주세요>>"))
                
                if choice == 1:
                    print("[국어성적 수정]")
                    print("-"*45)
                    print(f"현재성적: {s[2]}")
                    s[2] = int(input("수정할 국어성적을 입력해주세요: "))
                    s[5] = s[2]+s[3]+s[4] 
                    s[6] = s[5]/3
                    print(f"{name} 학생이 수정되었습니다.")
                elif choice == 2:
                    print("[영어성적 수정]")
                    print("-"*45)
                    print(f"현재성적: {s[3]}")
                    s[3] = int(input("수정할 영어성적을 입력해주세요: "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생이 수정되었습니다.")
                else:
                    print("[수학성적 수정]")
                    print("-"*45)
                    print(f"현재성적: {s[4]}")
                    s[4] = int(input("수정할 수학 성적을 입력해주세요: "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생이 수정되었습니다.")
        
        if temp == 0:
            print("학생을 찾지 못했습니다. 다시 입력해주세요")
            
        
        # 수정할 학생이 없는 경우
        temp = 0     
    
    elif choice == 4:
        pass
    elif choice == 0:
        pass