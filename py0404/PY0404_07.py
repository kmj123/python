# 파일 읽어오기
# 1. open() 2. f.read() 3. f.close()
# r:읽기, w:쓰기, a:이어쓰기
f = open("py0404/stu.txt","r",encoding="utf8")
# 1줄이면 여러줄이 반복문을 실행
students = []
while True:
    data = f.readline()
    if not data: break
    # data : 1,홍길동,60,100,100,260,86.666666666,3
    # strip() : 공백제거, strip() : 분리
    s = data.strip().split(",")
    
    # 아래의 모양처럼 만들기  
    # students = [
    #     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    #     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    #     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    # ]
    students.append({
        "no":int(s[0]),"name":s[1],"kor":int(s[2]),
        "eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),
        "avg":float(s[6]),"rank":int(s[7])
    })
    
    f.close()
    
    print(students)