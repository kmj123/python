students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

# sorted() 기존의 리스트은 유지, 새로운 리스트 생성
s_list = sorted(students, key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)


# sort() 기존의 리스트의 값을 변형시킴
# # 합계정렬 방법
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'])  # 합계 순차정렬
# print('-'*60)
# print(students)
# students.sort(key=lambda x:x['total'],reverse=True)  # 합계 역순정렬
# print('-'*60)


# 이름 정렬 방법
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['name'])   # 이름으로 순차정렬
# print(students)
# students.sort(key=lambda x:x['name'],reverse=True)  # 이름으로 역순정렬
# print("-"*60)


# dict 타입은 sort() 함수를 사용할 수 없음
# students.sort() 
# print(students)


# 리스트 sort() 정렬됨
# a_list = [20,50,10,40,90]
# a_list .sort()  # 순차정렬/ 오름차순
# print(a_list)
# a_list.sort(reverse = True)
# print(a_list)   # 역순정렬/ 내림차순



# 람다식 lambda -> 함수 축약형
# 람다식
# lambda 매개변수:리턴값
#lambda a:a*20

# map() 함수 : 리스트에 함수를 적용해서 다시 리스트로 반환
# filter() 함수: 리스트에 함수를 적용해서 조건에 맞는(True)것만 다시 리스트로 반환

# filter 함수 관련

 
# a_list = [1,2,3,4,5]    # list 모든값에 제곱을 해서 리스트를 생성
# aa_list = []
# for i in a_list:
#     aa_list.append(i**2)
    
    
# # map(함수, 리스트)
# def func(x):
#     return x**2
# print(list(map(func, a_list)))


# # 람다식 - mpa() 함수를 lambda를 사용하면 코드를 줄일 수 있음
# print(list(map(lambda x:x**2,a_list)))

