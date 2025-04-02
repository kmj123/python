i_list = [1,2,3,4,5,1,2,10]  # 리스트값 필요, list -> i_list 리스트명 변경했음
#key, value 필요 "key":value
dic = {"no":1, "name":"홍길동", "kor":100,"eng":90,"math":80,"total":270} 
print(dic)
txt_list = ['안녕','반가워','다음','내일','봐','잘','지내','봐요']

#------------------
# # 얕은 복사, 깊은 복사
# new_list = i_list   # 얕은 복사: new_list가 변경되면 i_list도 변경된다
# new_list2 = [*i_list]   # 깊은 복사: new_list2 따로 i_list 따로 생성된다.(보통은 깊은 복사 이용)

#------------------
# # zip
# for i,t in zip(i_list,txt_list):
#     print(i,t)
    
# # zip 사용해서 list 생성
# new_list = list(zip(i_list,txt_list))
# print(new_list)

# # zip 사용해서 dict 생성
# new_dic = dict(zip(i_list, txt_list))
# print(new_dic)


#------------------
# # 리스트 내포 
# # 1-10 까지 리스트 생성
# a_list = [i+1 for i in range(10)]
# print(a_list)

# b_list = [0]*10
# print(b_list)

# c_list = [i for i in range(1,51) if i%2==1]
# print(c_list)


#------------------
# # 딕셔너리 전체 출력
# for k in dic:
#     print(dic[k])
    
# for k,v in dic.items():
#     print(k,v)
    
# # 리스트 전체 출력
# for i in list:
#     print(i)


#------------------
# # 딕셔너리 정렬
# import operator
# dic_sort = sorted(dic.items(), key=operator.itemgetter(0))
# print(dic_sort)

# # 리스트 정렬
# list.sort()  # 리스트 순차정렬
# print(list)

# # 리스트 정렬
# list.sort(reverse=True) # 리스트 역순정렬
# print(list)


#------------------
# # 딕셔너리 key, values
# print(dic.keys())   # dict_keys(['no', 'name'])
# print(dic.values()) # dict_values([1, '홍길동'])
# print(dic.items()) # dict_items([('no', 1), ('name', '홍길동')]) 동시에 출력 = 튜플형태

# if 'no' in dic: # 딕셔너리를 비교할 때 key를 가지고 비교하게 됨.
#     print("있습니다.")


#------------------
# # 딕셔너리 개별 출력
# print(dic['no'])
# # print(dic['kor'])   # 키가 없는 것을 출력할 때 에러 KeyError: 'kor'
# print(dic.get('kor'))  # get() 함수 사용시 없는 키는 None 출력

# # 리스트 개별 출력 방법
# print(list[0])


#------------------
# # 딕셔너리 수정
# dic['name'] = "유관순"
# print(dic)

# list[0] = 100
# print(list)


#------------------
# # 딕셔너리 삭제
# del dic["no"]
# print(dic)

# # 리스트 삭제
# del list[0]
# print(list)


#------------------
# # 딕셔너리 추가
# dic['kor'] = 100
# print(dic)

# # 리스트 추가
# list.append(100)
# print(list)