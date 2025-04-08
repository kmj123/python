
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0

while True:
    print("[학생성적프로그램]")
    print("[1. 학생성적 입력]")
    print("[2. 학생성적 출력]")
    print("[3. 학생성적 수정]")
    print("[4. 등수처리]")
    print("[0.프로그램 종료]")
    choice = int(input("원하는 번호를 입력하세요>>"))
    
    if choice == 1:     #학생성적 입력
        while True:
            print("[학생성적입력]")
            no = count
            name = input(f"{no}번 학생의 이름을 입력해주세요>>")
            
            while True:
                kor = int(input("국어점수>> "))
                if 0 <= kor <= 100:
                    break
                else: 
                    print("0~100 사이의 숫자를 입력해주세요")
                    print("숫자만 가능합니다.")
                
            while True:
                eng = int(input("영어점수>> "))
                if 0 <= eng <= 100:
                    break
                else: 
                    print("0~100 사이의 숫자를 입력해주세요")
                    print("숫자만 가능합니다.")
                
            while True:
                math = int(input("수학점수>> "))
                if 0 <= math <= 100:
                    break
                else: 
                    print("0~100 사이의 숫자를 입력해주세요")
                    print("숫자만 가능합니다.")
                
        
            total = kor+eng+math
            avg = total/3
            rank = 0
        
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank})
            
            print(f"{no}번 {name}학생이 등록되었습니다.")
            count += 1
            
    
    elif choice == 2:       # 학생성적 출력
        print("[ 학생성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        
        for s in students: 
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")
            
    
    elif choice == 3:       # 학생성적 수정
        print("[ 학생성적 수정 ]")
        name = input("수정할 학생의 이름을 입력하세요>>")
        temp = 0
        
        for s in students:
            if s['name'] == name:
                temp = 1
                print(f"{name} 학생을 찾았습니다. 성적을 수정합니다.")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                choice = int(input("원하는 번호를 선택하세요"))
                
                if choice == 1:
                    pre_kor = s['kor']
                    print(f"현재 국어점수: {pre_kor}")
                    s['kor'] = int(input("수정할 국어점수: "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
                    print(f"국어점수 {pre_kor}에서 {s['kor']}로 변경되었습니다.")
                    
                if choice == 2:
                    pre_eng = s['eng']
                    print(f"현재 영어점수: {pre_eng}")
                    s['eng'] = int(input("수정할 영어점수: "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
                    print(f"영어점수 {pre_eng}에서 {s['eng']}로 변경되었습니다.")
                    
                if choice == 3:
                    pre_math = s['math']
                    print(f"현재 수학점수: {pre_math}")
                    s['math'] = int(input("수정할 수학점수: "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    
                    print(f"수학점수 {pre_math}에서 {s['math']}로 변경되었습니다.")
        
        if  temp == 0:
            print(f"{name} 학생을 찾지 못했습니다.")
    
    elif choice == 4:       # 등수처리
        print("[ 등수처리 ]")
        for s in students: 
            num = 1
            for ss in students:
                if s['total'] < ss['total']:
                    num += 1
            s['rank'] = num
            
        print("등수처리가 완료되었습니다.")
        print()            
    
    elif choice == 0:
        print("[프로그램 종료]")
        break
    
