# 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현

# 입력한 숫자
# for i in range(10):
#     num = int(input("숫자를 입력하세요>>"))
#     # num 가 num_list에 있는지 확인해서 없으면 입력시키고, 있으면 제외
    
#     if num not in num_list:
#         num_list.append(num)

num_list = []
i = 0
while i < 10: 
    num = int(input("{}번째 숫자를 입력하세요>>".format(i+1)))
    if num not in num_list:
        num_list.append(num)
        i += 1

print(num_list)

# input_list = [1,5,10,9,8,20]

# a = 5
# # in 명령어로 객체가 객체 리스트 안에 있는지 확인 가능
# if a in input_list:  # input_list 안에 a가 있는지 확인
#     print("{}가 존재합니다.".format(a))
# else: 
#     print("{}}가 존재하지 않습니다.".format(a))



# i = 0
# while i < 10:
#     print(i)
#     i += 1


# i = 0

# # 반복문 whil - 조건이 맞으면 무한 반복 가능
# while i <10:
#     print(i)
#     i += 1 # 1씩 증가 
# print("-"*50)      

# # 반복문for  -  횟수만큼 반복
# for j in range(10):
#     print(j)