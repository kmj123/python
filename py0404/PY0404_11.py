from StuFunc import *
import random   
    
students = []
# 파일 읽어오기

with open("py0404/stu.txt","r",encoding="utf8") as f:
    while True:
        data = f.readline() # 1,홍길동,60,100,100,260,86.66666667,3
        if not data: break  # '' 공백이면 반복문종료
        s = data.strip().split(",") # strip(): 공백제거 strip(): 분리
        students.append({
            "no":int(s[0]),"name":s[1] ,"kor":int(s[2]) ,"eng":int(s[3]) ,
            "math":int(s[4]) ,"total":int(s[5]) ,"avg":float(s[6]) ,"rank":int(s[7])
        })

# count = 4 while문으로 반복할거라 의미가 없어짐
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
# 최대값 +1 증가
count = max(students, key=lambda x:x['no'])['no']+1
    
while True:
    print("[ 학생성적 프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("7. 학생성적저장")
    print("0. 프로그램 종료")
    choice = int(input("원하는 번호를 입력하세요>>"))
    
    if choice == 1:
        print("[학생성적입력]")
        print("-"*60)
        no = count
        name = input("등록할 학생의 이름을 입력해주세요>>")
        # while True:
        kor = int(input("국어성적: "))
        eng = int(input("영어성적: "))
        math = int(input("수학성적: "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        
        students.append({
            "no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank
        })
        
        print(f"{no}번 {name}학생이 등록되었습니다.")
        print()
    
        count += 1
        
    elif choice == 2:
        print("[학생성적출력]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        
        
    elif choice == 3:
        temp = 0
        print("[학생성적수정]")
        print("-"*60)
        name = input("수정할 학생의 이름을 입력해주세요>>")
        while True:
            for s in students:
                if temp == 1:
                    print(f"{no}번 {name} 학생을 찾았습니다. 수정할 과목을 선택해주세요>>")
                    
                    
                elif temp == 0:     
                    print(f"{no}번 {name}학생을 찾지 못했습니다. 다시입력해주세요!")
            
        
    elif choice == 4:
        print("[등수처리]")
        
    elif choice == 5:
        print("[학생성적정렬]")
        
    elif choice == 6:
        print("[학생성적삭제]")
        
    elif choice == 7:   # stu.txt에 데이터 저장
        print("[학생성적저장]")
        with open("py0404/stu.txt","w",encoding="utf8") as f:
            for s in students:
                data = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']},{s['rank']}\n"
                f.write(data)
        print("파일 저장완료")    
        print()
        
    elif choice == 8: 
        print("[프로그램 종료]")
        break