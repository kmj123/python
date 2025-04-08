# []가 3번 중첩되어 있는 리스트
a = [[1,2,3],[[4,[5,6]],7,[8,9]]]

def flatten(data):
    output = []
    for i in data:
        if type(i) == list:
            output.extend(flatten(i))    # 재귀함수호출
        else:
            output.append(i)
    return output
print(a)
print("-"*60)
print(flatten(a))       


# fssssor i in a:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     print(k, end=" ")
#             else: 
#                 print(j,end=" ")
            
#     else:        
#         print(i, end=" ")