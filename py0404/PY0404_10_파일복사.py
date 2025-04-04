# 문서읽어오기
# 일반파일 읽어오기
f = open("py0404/a.jpg","rb")   # 파일 읽기
ff = open("c:/down/b.jpg","wb") # 파일 쓰기

# 이진파일은 용량이 클수 있으므로, 1byte 읽어오기
while True:
    fData = f.read(1)
    if not fData: break
    # len = ff.write(fData)
f.close()
print("파일 읽어오기 완료")

# 문서저장 - w,a
# 파일저장 - wb
# 폴더 존재 확인: os.path.exist()
# 폴더생성: os.makedir(): 폴더 1개 - c:/down1/aaa/a.jpg
# 폴더생성: os.makedirs(): 모든 폴더생성 - c:/down1/aaa/a.jpg
import os
# 폴더가 없으면 생성 후 진행
if not os.path.exists("c:/down1"):
    os.makedirs("c:/down1")
ff = open("C:/down/b.jpg","wb")
len = ff.write(fData)
print(f"파일크기 : {len} 바이트")
ff.close()

print("파일 저장완료")