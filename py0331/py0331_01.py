a = 10
a_list = [1,2,3,4,5]

print("a : ",a)
print("a_list : ",a_list)

a_list[0] = 100
print("a_list = ",a_list) # [100,2,3,4,5]

# a변수와 b변수는 다른 변수임
b = a
b  = 1000
print("a : ",a) # 10
print("b : ",b) # 1000

#새롭게 복사 : 깊은복사
a_list = [1,2,3,4,5]
b_list = [*a_list]
b_list[1] = 200

print()
print(a_list)


### 주소값 복사 = 얕은 복사
# a_list = [1,2,3,4,5]
# b_list = a_list
# b_list[1] = 200

# print(a_list) # a_list를 b_list에 귀속시키므로써 b_list 변경시 a_list도 같이 변경됨


# a_list = [1,2,3,4,5]
# sum = 0
# for i in a_list:
#     sum = sum + 1
    
#     print(sum) # = 1,2,3,4,5
# #print(sum) = 5


# 구구단
# 2 X 1 = 2 형식을 출력됨
# for i in range(2,10):
#     print("{} 단".format(i))    # 위의 수식 처리하고 단 나오고 처리하고 단 나옴
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print() # 단과 단 사이에 공백을 만들어주려면 위의 print보다 앞에 나와야한다.