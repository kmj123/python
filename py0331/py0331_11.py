import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]
        
while True:
    print("[  좌표 맞추기 게임  ]")
    print("-"*45)
    print("   |",end="\t")
    
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)
    
    for i in range(5):
        print(f"{i}  |",end="\t")
        for j in range(5):
            print(a_list[i][j],end="\t")
        print()
    
    print("-"*45)
    num = int(input("1-25 숫자 입력: "))
    if num > 25:
        print("다시 입력해주세요!")
    
    for i in range(5):
        for j in range(5):
            if a_list[i][j] == num:a_list[i][j] = "X"
            
    print()