
# zip(0) -> 2개 리스트를 합치는 것 -> list타입변경, dict 타입변경 가능
n_list = ['홍길동','유관순','이순신','강감찬','김구']
t_list = [100,99,89,79,100]
a_list = [10.0,9.0,8.0,7.0,10.0]


print(list(zip(n_list,t_list,a_list))) # 수정불가/ 두가지 이상 합치기 가능
print(dict(zip(n_list,t_list))) # 수정가능/ 두가지 이상 합치기는 불가능

# zip ; [('홍길동', 100), ('유관순', 99), ('이순신', 89), ('강감찬', 79), ('김구', 100)]
# 튜플에 있는 형태로 출력된다.
#tuple_list = list(zip(n_list,t_list))


# students = {"no":1,"name":"홍길동", "kor":100}
# for key,value in students.items():
#     print(f"{key} : {value}")

# 아래코드는 값을 받아 올수없음
# for key,value in enumerate(students):
#     print(f"{key} : {value}")

# # 2개의 리스트를 출력할 수 있음.
# n_list = ['홍길동','유관순','이순신','강감찬','김구']
# t_list = [100,99,89,79,100]
# for n,t in zip(n_list,t_list):
#     print(f"{n} : {t}")


# # 리스트 내포 : if 조건절을 넣을 수 있음(한 줄만 가능)
# n_list = [i for i in range(1,51) if i%3==0]
# print(n_list)

# 
# list = [1,2,3,4,5]
# # list +100*100
# # list2 = ['10,000','10,200','10,300','10,400','10,500']
# # list2 = [i+100 for i in list]
# # print(list2)

# # format함수 천단위 표시 @@외우기!!!@@
# list2 = ["{:,d}".format((i+100)*100) for i in list]

# print(list2)
#------------------------------------------
# set -> 중복을 제거해서 키를확인
# myset1 = {1,2,2,3,3,3,5,5,7}
# print(myset1)

# menu_list = ['삼각김밥', '바나나', '삼각김밥', '사과', '바나나','도시락', '삼각김밥']
# print(set(menu_list))   # list타입을 set타입으로 변경해서 확인