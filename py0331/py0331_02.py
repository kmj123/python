#삭제 del, pop, remove, clear
a_list = [1,2,3,4,5]
del a_list[2]   # 위치값 삭제
print(a_list) 

a_list.pop()    # 맨 뒤의 값, 특정위치의 값 삭제
print(a_list)   

a_list.remove(1) # 데이터 값으로 삭제
print(a_list)   

a_list.clear()     # 전체 삭제
print(a_list)



# # 리스트 추가 : append, insert, extend
# a_list = [1,2,3]
# a_list.append(4) # 맨 뒤에 값을 추가(하나의 값만 추가)
# print(a_list)
# a_list.insert(1,100) # 1이라는 위치에 100을 넣어라(특정위치에 값을 추가)
# print(a_list)
# a_list.extend([100,200,300]) # 다른 리스트를 추가
# print(a_list)



# # 리스트 내포 
# a_list = [i for i in range(1,11)]
# print(a_list)


# # 리스트 - append 추가방법
# a_list = []
# for i in range(1,11):
#     a_list.append(i) 
    
# print(a_list)


# # index 번호를 넣으려면, enumerate를 사용
# a_list = [237,10,5,9,100,1000,50]
# for idx,value in enumerate(a_list):
#     print(f"(idx+1) : (value)")