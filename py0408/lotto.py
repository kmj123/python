# lotto 프로그램/ py0328_08.py
import random
# 6개 숫자 랜덤번호 생성    
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력

my_lotto=[0]*6
win_lotto = []
lotto = [i+1 for i in range(45)]    # 로또 랜덤번호
lotto2 = [i+1 for i in range(45)]   # 
def lotto_mix():
    global lotto,lotto2
    random.shuffle(lotto)

lotto_mix()
while True:
    print("[ 로또 맞추기 프로그램 ]")
    print("-"*40)
    print('1. 로또 다시 생성')
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가 입력한 로또번호 확인")
    print("-"*30)
    print()
    choice = int(input("원하는 번호를 입력하세요"))
    
    if choice == 1: # 랜덤번호 생성
        lotto_mix()
        print("번호를 다시 생성했습니다.")
    
    elif choice == 2:   # 번호 입력: 1-45 까지의 숫자 중 6개를 입력받아 리스트에 저장하기
        count = 0
        while True:
            print("[ 로또번호 입력 ]") 
            print("-"*30)
            # 로또 순번 출력 / 7X5 배열 화면 출력
            for i in range(45):
                if i == 0 : pass
                if i%7 != 0:
                    print(lotto2[i], end="\t")
                else: 
                    print()
                    print(lotto2[i], end="\t")
            print()
            
            choice = int(input("원하는 번호 입력 (0. 이전화면 이동)"))

            # 1-45까지의 수를 입력 후 화면에 X 표시하기
            if choice < 0 or choice > 45:
                print(f"{choice}는 없는 번호입니다. 다시입력해주세요>> ")
                continue
            
            temp = 0 
            for i in lotto2:
                if i == choice:
                    lotto2[i-1] = "X"   # choice=5 인 경우 좌표는 4이기때문에 -1 해준다
                    my_lotto[count] = choice
                    count += 1
                    temp = 1
                if temp == 0:
                    print(f"{choice}는 입력한 번호입니다. 다시 입력해주세요")
                if count >= 6:
                    print("로또번호를 6개 모두 입력하셨습니다.")
                    break
    
        
    elif choice == 3:
        print("[ 로또번호 당첨확인 ]")
    
    elif choice == 4:
        print("[ 로또리스트 모두 확인 ]") 
    
    elif choice == 5:
        print("[ 내가 입력한 로또 번호 확인 ]")

