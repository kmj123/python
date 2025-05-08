from pyFunc import *


while True:
    print("[ 학생 성적 프로그램 ]")
    print("1. 학생전체출력")
    print("2. 학반별 최고등수 출력")
    print("3. 학반별 최하등수 출력")
    print("4. 부서별 최고연봉 출력")
    print("5. stuscore2 학반 부여(1-10,1...)")
    print("6. 회원정보 11-20 출력")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요>>"))
     
    # 학생전체출력
    if choice == 1:
        stuPrintAll()
    
    # 학반별 최고등수 출력
    elif choice ==2:
        conn = connections()
        cursor = conn.cursor()
        sql = "select * from stuscore2 a\
                where total in(\
                select max(total) maxtotal from stuscore2 b \
                where a.sclass=b.sclass\
                group by sclass)"
                
        cursor.execute(sql)
       
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print("최고점수 출력 완료")
        print()
        
        cursor.close()
        conn.close()
    
    # 학반별 최하등수 출력
    elif choice ==3:
        conn = connections()
        cursor = conn.cursor()
        sql = "select * from stuscore2 a\
                where total in(\
                select min(total) from stuscore2 b\
                where a.sclass=b.sclass\
                group by sclass)"
                
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        
        print("최하점수 출력 완료")
        print()
        
        cursor.close()
        conn.close()
        
    # 부서별 최고연봉 출력
    elif choice ==4:
        conn = connections()
        cursor = conn.cursor()
        sql="select employee_id,emp_name,salary,department_id from employees a\
            where salary in(\
            select max(salary) from employees b\
            where a.department_id=b.department_id\
            group by department_id)\
            order by department_id"
            
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        for r in rows:
            print(r)
            
        cursor.close()
        conn.close()
                
    elif choice ==5:
        conn = connections()
        cursor = conn.cursor()
        sql = "update stuscore2 set sclass = \
                case\
                when sno between 1 and 10 then 1\
                when sno between 11 and 20 then 2\
                when sno between 21 and 30 then 3\
                when sno between 31 and 40 then 4\
                when sno between 41 and 50 then 5\
                when sno between 51 and 60 then 6\
                when sno between 61 and 70 then 7\
                when sno between 71 and 80 then 8\
                when sno between 81 and 90 then 9\
                when sno between 91 and 100 then 10\
                else 11\
                end"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    
        print("완료")
        
    if choice == 6:
        pass
        
    else: break