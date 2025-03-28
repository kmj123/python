#
num = 7
if 10>=num and num>=0:
    print("10에 해당되는 숫자입니다.")
    
#3,4,5 -> 봄의 계절입니다
# 6,7,8, -> 여름
# 9,10,11 -> 가을
# 12, 1,2 겨울

season = int(input("월을 입력하세요.>>"))
if 5 >= season >= 3:
    print("봄입니다.")
elif 8>= season >= 6:
    print("여름입니다.")
elif 11>= season >= 9:
    print("가을입니다.")
else:
    print("겨울입니다.")
    


