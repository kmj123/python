import dbconn

    
print("--------------------db연결----------------------")
# db접속
conn = dbconn.connections()    # sql dev 프로그램 오픈
cursor = conn.cursor()  # sql창 오픈
## employees 월급이 4000~6000 사이의 사번,이름,월급

name = input("검색하려는 이름을 입력하세요>>")

#query = "select employee_id,emp_name,salary from employees where salary between 4000 and 6000"
name = '%' +name +'%'
query = "select employee_id,emp_name,salary from employees where emp_name like :name "
cursor.execute(query,name=name)
# cursor.execute("select * from stuscore where sno>=90")  # sql 구문 F9 실행
rows = cursor.fetchall() # 데이터 불러오기

for r in rows:
    print(r[0],r[1],r[2])


