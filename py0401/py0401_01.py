# 1차원 리스트
#s_list = [i+1 for i in range(25)]

import random
# 1차원 리스트 생성
s_list = [i for i in range(1,26)]   

#random.random(), random.randint(), random.sample(), random.shuffle()
random.shuffle(s_list)  
print(s_list)

# 2차원 리스트
my_list = [[0]*5 for _ in range(5)] # _ 또는 i 사용 가능
print(my_list)  #[0,0,0,0,0][0,0,0,0,0][0,0,0,0,0][0,0,0,0,0][0,0,0,0,0]

my_list [0][1] = 1     # 값 변경
print(my_list)         #[[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# 1 차원 리스트 값 -> 2차원 리스트 입력
for i in range(5):
    for j in range(5):
        my_list[i][j] = s_list[5*i+j]   # 5차원 배열 공식: 5x+y
        
# 화면 출력
while True:
    print(" "*10,end="")
    print("  [  좌표 맞추기 게임  ]  ")
    print("-"*45)
    print("*  |",end="\t")

    for i in range(5):
        print(i,end="\t")       
    print()
    print("-"*45)
    #-----------------------------------
    # 0       1       2       3       4
    #-----------------------------------

    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(my_list[i][j],end="\t")
            #print() 계속 줄바꿈됨
        print() # 5개 찍고 줄바꿈
        
    print("-"*45)
    
    # 번호 입력 X 표시
    num = int(input("1-25 숫자입력: "))
    if num > 25:
        print("다시 입력해주세요")
    
    # 25개 모두 비교
    stop = 0
    for i in range(5):
        for j in range(5):
            # if my_list[i][j] == num: my_list[i][j] = "X"
            if my_list[i][j] == num:
                my_list[i][j] = "X"
                stop = 1
                break
        if stop == 1: break
    print()
    
    # 좌표 입력 X 표시
    # x = int(input("X좌표를 입력하세요>>"))
    # y = int(input("y좌표를 입력하세요>>"))

    # my_list[y][x] = "X"
    