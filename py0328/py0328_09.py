# 구구단을 출력하시오
# 2 X 1 = 2

for i in range(1,10):
    
    #print("[{}단]".format(i))
    
    for j in range(2,10):
        print("{} X {} = {}".format(j,i,i*j), end="  ")
    print()




## 은행가면 001 002 003... 010 011 012... 999 
# for i in range(1,1000):
#     print("{:03d}".format(i))