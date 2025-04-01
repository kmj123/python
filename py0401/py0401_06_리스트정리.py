a_list = [1,2,3,"홍길동",4,5,6,7,10,11,12,13]



# 1. 리스트 삭제 명령어
del a_list[0]   # index 번호를 가지고 삭제
a_list.pop()    # 마지막데이터 삭제
a_list.pop(2)   # index 번호 삭제
a_list.remove(11)    # 11라는 값을 삭제
a_list.clear()  # 모두삭제

print(a_list)
#--------------------------------

# 2. 리스트 추가
a_list.append(1)    # 리스트 마지막에 추가
a_list.append(2)
a_list.insert(0,'홍길동')   # 원하는 위치열에 값 추가
a_list.extend([10,11,12])   #리스트 추가

print(a_list)

#------------------------
# 3. 리스트 수정
a_list[0] = "유관순"

print(a_list)

#-------------------------
# 4. 리스트 출력
for a in a_list:
    print(a)
    
#-------------------------
# 5. 리스트에 여러데이터 묶음도 추가 가능 - 리스트안에 리스트 추가가능
a_list.append(['컴퓨터공학','소프트웨어공학','무역학과'])
print(a_list)

#-------------------------
# 6. 리스트 길이
print(len(a_list))

#--------------------------
s_list = [1,2,3,1,2,2,2,1,3,4,5,7,7,7,7]
num = 0
for s in s_list:
    if s == 1: num+= 1 
print("{} : {}".format(1,num))

#----------------------------
# 리스트 정렬
s_list.sort()   # 순차정렬, 낮은 순 정렬
print(s_list)
s_list.sort(reverse=True)
s_list.reverse()# 역순정렬, 높은순 정렬
print(s_list)