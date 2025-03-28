# 달러를 입력하면, 원화 환산해서 출력하시오.
# 1$ -> 1467원 환산
# 120$ -> 120*1467

# money = int(input("달러를 입력하세요.>> "))
# won = money*1467
# #소수점 자리 출력 = :.2f / 천 단위 출력 = :,d
# print("입력한 달러: {:,d}달러/ 한화{:,d} 원".format(money, won))

# 1779원 -> 동전으로 변경을 하려고 합니다.
# 500원 3개, 100원 2개, 50원 1개, 10원 2개, 1원 9개
# money = int(input("동전으로 변경할 금액을 입력하시오.>>"))
# ch500 = money//500
# ch100 = (money%500)//100
# ch50 = ((money%500)%100)//50
# ch10 = (((money%500)%100)%50)//10
# ch1 = ((((money%500)%100)%50)%10)//1

# print("500원 {}개\t100원 {}개\t50원 {}개\t10원 {}개\t1원{}개".format(ch500,ch100,ch50,ch10,ch1))

#--------------------------------------------------------------------------------------------------------

# 원의 넓이 : 3.14 X 반지름 X 반지름
# 원의 둘레 : 2 X 3.14 X 반지름
# 반지름을 입력받아, 원의 넓이를 구하는 프로그램을 구현하시오.

# 출력: 
# 원의 넓이 : 100 cm2
# 원의 둘레 : 50 cm

len_input = int(input("반지름을 입력하시오.>>"))
in_dim = 3.14*(len_input**2)
in_circum = 2*3.14*len_input

print("원의 넓이 : {:.2f}cm2".format(in_dim))
print("원의 둘레 : {:.2f}cm".format(in_circum))

# 직사각형 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.
width = int(input("직사각형의 가로 길이를 입력하시오>>"))
height = int(input("직사각형의 세로 길이를 입력하시오>>"))
square_dim = width*height
square_circum = (width*2)+(height*2)

print("직사각형의 넓이: {}cm2".format(square_dim))
print("직사각형의 둘레: {}cm".format(square_circum))

