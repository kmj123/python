# 파일입출려기 : 파일열기 - 파일읽기, 파일쓰기 - 파일 닫기
# 파일열기 - 3가지 모드 : r:읽기모드, w: 쓰기모드, a: 추가모드, b: 이진파일 - 파일복사
# f = open("a.txt","r")   # 읽기모드
# f= open("a.xtx","w")    # 쓰기모드
# f = open("a.txt","a")   # 추가모드

# news.txt 파일 출력하시오
f = open("py0404/news.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()



# 파일 읽어오기
#f = open("C:/workspace/python/a.txt","r",encoding = "utf-8")
# f = open("py0404/b.txt","r",encoding="utf-8")   # 폴더안에 있는 파일 읽어오기
# for line in f:
#     print(line.strip())
# f.close()


# while True: # 3줄까지 있으면 그 다음부터는 빈공간이 계속 생기게 됨
#     line = f.readline()
#     if not line: break # 빈공간이 있으면 while문을 빠져나오게 만들어야함.
#     print(line.strip())
    

# 파일읽기 = readliner() : 모두읽어오기
# f = open("a.txt","r",encoding ="utf-8")
# lines = f.readlines( ) # 모두읽어오기
# for line in f():
#     print(line.strip())
# f.close()

# # 파일읽기 - r 1줄 읽기
# f = open("a.txt","r",encoding="utf-8")
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close()



# print("완료되었습니다.")