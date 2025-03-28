# 3가지 조건문 서식: 
# if, if~else, if~elif~else
# 음수, 0, 양수

# num = int(input("숫자를 입력하세요.>>"))
# if num>0:
#     print("양수입니다.")
# elif num == 0:
#     print("0입니다.")
# else:
#     print("음수입니다.")

# 시험성적을 입력받아
# 60점 이상이면 합격, 미만이면 불합격 출력하시오

# num = int(input("성적을 입력하시오>>"))

# if num >= 60:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")
    
# # 70점 이상 합격, 69~60점 재시험, 60점 미만 불합격
# num = int(input("성적을 입력하시오>>"))

# if num >= 70:
#     print("합격입니다.")
# elif num >= 60:    # 위에 조건문에서 70점 이상은 걸러지기 때문에 69 >= num 은 필요없다
#     print("재시험입니다.")
# else:
#     print("불합격입니다.")
    
# # 시험 -> 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, F
# 100 ~ 97점 A+, 96~93점 A, 92~90점 A-, 89~87점 B+, 86~83점 B, 82~80 점 B-
score = int(input("점수를 입력하세요.>>"))

if score >= 90:
    print("A", end="")
    if score >=97:print("+")
    elif score >= 93: pass
    else: print("-")
    
elif score >= 80:
    print("B", end="")
    if score >= 87: print("+")
    elif score >= 83: pass
    else: print("-")
    
elif score >= 70:
    print("C", end="")
    if score >= 77: print("+")
    elif score >= 73: pass
    else: print("-")
    
elif score >= 60:
    print("D", end="")
    if score >= 67: print("+")
    elif score >= 63: pass
    else: print("-")
    
else:
    print("F")

# print("안녕", end="") # 줄바꿈삭제: end=""
# print("하세요")