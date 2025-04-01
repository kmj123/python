students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.6,"rank":2}
]

count = 4   # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True: 
    print("[  학생 성적 프로그램  ]")
    print("-"*45)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 프로그램종료")
    print("-"*45)
    choice = int(input("원하는 번호를 입력하세요>>"))

    if choice == 1:
        no = count
        print("[  학생성적입력  ]")
        name = input("학생이름을 입력하세요>>")
        if name == 0: break
            
        # 성적입력
        kor = int(input("국어성적을 입력하세요>>"))
        eng = int(input("영어성적을 입력하세요>>"))
        math = int(input("수학성적을 입력하세요>>"))
        total = kor+eng+math
        avg = total/3
        rank = 0
        
        students.append("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print(f"{name} 학생이 등록되었습니다.")
        print()
        
        count += 1
        
    elif choice == 2:
        print("[  학생성적 출력  ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*45)
        print()
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))
            print()
        
    elif choice == 3:
        print("프로그램을 종료합니다.")

        



