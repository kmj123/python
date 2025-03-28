# # 반복문을 사용해서 1-10까지 출력
# for i in range(1,11):
#     print(i)
    
# a = 10
# if a<9 and a> 5:  #True and Fals 둘다 만족시켜야함
#     print(a)

# if a> 5 or a < 9: #True or False 둘중 하나만 만족하면됨
#     print(a)
    
# a_list =[1,2,3,4,5]
# print(a_list[2])
# print(a_list[1:4]) # [시작위치 : 끝나는 위치] - 슬라이싱
# print(a_list[:3]) # [끝나는 위치-1] - 처음부터 시작해라
# print(a_list[2:]) # [시작위치] - 끝까지 출력
# print(a_list[::2]) # 2개씩 증가해서 출력
# print(a_list[::3])
# print(a_list[::-1]) # 역순으로 출력
# print(a_list[:-1])

# a = "안녕하세요"
# print(a[2])
# print(a[1:4])
# print(a[:3])
# print(a[::3])
# print(a[2:1])
# print(a[::-1])
# print(a[:-1])

# print(a[:7]) # 슬라이싱은 없는 값 출력시 에러가 나지 않음
# print(a[7]) # 인덱싱 없는 것 출력시 에러 indexError

# print(len(a_list)) # 리스트 개수 확인
# print(a_list[:len(a_list)-1])
# print(len(a)) #문자열 길이

# # a_list[1:11:2]
# for i in range(1,11,2):
#     print(i, end="") # end = "" 줄바꿈없이 출력

#break
sum = 0
i=0
for i in range(1,100+1):
    sum = sum+i
    print("i: {}, sum: {}".format(i, sum))
    if sum >= 100: break

# print("1-100까지 합계: {}".format(sum))
print("sum이 100 넘었을때 i 값 : {}".format(i))
print("합계가 100이 넘었을때 sum 값: {}".format(sum))

# 합계가 100 넘는 위치의 숫자는 얼마일까요?
# 1+2+3+4+5+6+7+8+9+...합계가 100 넘는 위치 어디인지 출력하시오. 그때 값도 출력하시오
