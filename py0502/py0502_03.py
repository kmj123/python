### 학생성적프로그램에서 1명의 학생을 등록해보세요
from stuMain import *
conn = connections()
cursor = conn.cursor()


if choice == 1:
    name = input("등록할 학생의 이름을 입력해주세요>>")
    kor = int(input("국어점수를 입력해주세요>>"))
    eng = int(input("영어점수를 입력해주세요>>"))
    math = int(input("수학점수를 입력해주세요>>"))
    total = kor+eng+math
    avg = total/3
    rank = 0

    query = "insert into stuscore values(stuscore_seq.nextval,:name1,:kor1,:eng1,:math1,:total1,:avg1,0)"
    cursor.execute(query,name1=name,kor1=kor,eng1=eng,math1=math,total1=total,avg1=avg)
    conn.commit()
    print(name,"학생이 등록되었습니다.")
    print()

if choice == 2:
    query= "select * from stuscore"
    cursor.execute(query)   
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    print() 
    