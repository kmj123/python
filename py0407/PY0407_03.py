print(1)
print(2)
raise NotImplementedError   # 프로그램 구현이 아직 진행이 안되었음.
print(3)

# try:    # 프로그램 구현 부분
#     print(1)
#     print(2)
#     # raise NotImplementedError # 예외를 강제로 발생시킴
#     raise ZeroDivisionError # 
#     # choice = int(input("숫자를 입력하세요>>")) # 문자입력
#     print(3)
#     print(4)
# except Exception as e: # 프로그램 에러 발생시 구현
#     print(e)
#     print(5)
    
# else:   # 프로그램 에러가 미발생시 구현
#     print(6)
# finally:    # 에러와 상관없이 모든 상황에서 구현
#     print(7)


# try:
#     num = int(input("원의 반지름을 입력하세요>>"))
#     print("원의 넓이: ",3.14 * num**2)  
# except Exception as e:
#     print(e)
# else:  # else로 따로 빼지 않고 try 구문에 넣어도 상관없음
#     pass



# a_list = ["52",'273',"32","파이썬","103"]

# list_number = []
# # 숫자로 변환되는 것만 list_number 저장하시오.
# # if문 사용, 예외처리해서 사용

# # 예외처리 사용 - a_list 변환
# for a in a_list:
#     try: list_number.append(int(a))
#     except Exception as e: print("e")
        
# print("리스트 출력: ",list_number)



# # if문사용 a_list 변환
# for a in a_list:
#     if a.isdigit():
#         list_number.append(int(a))
#     else: 
#         print("숫자가 아님: ",a)
# print("리스트 출력: ", list_number)
