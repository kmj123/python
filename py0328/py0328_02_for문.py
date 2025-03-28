print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

# for 받을 값 in range(반복할 횟수):
#     print("")
# range(3) -> 0,1,2 총 세번을 돌게 되어있다.
for i in range(3):
    print("안녕하세요")
    
# range(1,4) -> 1,2,3 : 4앞에 까지 출력
for i in range(1,4):
    print("안녕하세요", i) 
    
for i in range(1,3+1):
    print('안녕하세요', i)
   
# range(1,11,3) : (시작번호, 마지막번호-1 만큼, 간격)
for i in range(1,11,3): 
    print("안녕", i)

# range() 자리에 list타입 가능    
a_list = [1,2,3,4,5]
for i in a_list:
    print("안녕",i)
    