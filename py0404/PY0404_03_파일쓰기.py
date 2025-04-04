# # 파일 이어쓰기 - a (있는글에 이어쓰기)
# f = open("py0404/memo2.txt","a",encoding = "utf-8")
# f.write("1,홍길동,100,100,90\n")
# f.close()

# f = open("py0404/memo2.txt","a",encoding = True)
# f.write("2,유관순,50,50,50\n")
# f.close()



# 파일쓰기 - w (모두삭제 후 다시쓰기)
f  = open("py0404/memo.txt","w",encoding="utf-8")
print("[ 메모장 ]")
print("----------")
print("저장하려는 글자를 입력하세요(x. 종료)")
while True: 
    line = input("")
    if line.lower() == "X": break
    f.write(line+"\n")
f.close()

# print("글쓰기 종료")


# 안녕하세요. 글자를 10번 반복해서 저장하시오.
# 안녕하세요
# f = open("py0404/aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write(f"{i+1}.안녕하세요\n")
# f.close()

# f = open("aa.txt","w",encoding="utf-8")

# f.write("안녕하세요\n") #\r: 문장에 끝으로 이동, \n: 줄바꿈
# f.write("반가워요\n")
# f.close()

# print("글쓰기 종료")