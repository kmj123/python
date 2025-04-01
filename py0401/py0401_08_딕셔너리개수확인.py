list = ["지드래곤","세븐틴","제니","리쿠","에스파"
        "지드래곤","리쿠","리쿠","세븐틴","세븐틴",
        "지드래곤","지드래곤","지드래곤","세븐틴","세븐틴",
        "제니","제니","제니","제니","제니",
        "에스파","지드래곤","에스파","세븐틴","에스파",
        "리쿠","리쿠","리쿠","리쿠","리쿠",
        ]

singer = {}
## 각각의 가수가 몇번 존재하는지 출력하시오.
# "지드래곤" : 6
for i in list:
    if i not in singer:
        singer[i] = 1
    else: 
        singer[i] = singer[i]+1 #singer[i] += 1

for i,v in singer.items(): #(key,value) for i,v in enumerate(singer):
    print(f"{i} : {v}")
    
        

# list = [1,2,3,1,2,3,5,6,8,9,10,1,2]
# dic = {}

# for i in list:
#     # dic에 추가, dic 키가 존재하는지 확인
#     if i not in dic:
#         dic[i] = ""
#     # dic[i] = dic[i] + 1 # 키가 몇개 존재하는지 개수 파악
#     dic[i] += "■"

# for i,d in enumerate(dic):
#     print(f"{i} : {dic[d]}")

# print(dic)

# # dic = {1:3, 2:3, 3:2, 5:1, 6:1, 8:1, 9:1, 10:1} 