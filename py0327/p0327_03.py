# 학생 성적 프로그램
# 이름, 국어, 영어, 수학 입력받아, 합계, 평균을 구하는 프로그램을 구현

name = input("이름을 입력하세요>>")
kor = int(input("국어성적을 입력하세요>>"))
eng = int(input("영어성적을 입력하세요>>"))
math = int(input("수학성적을 입력하세요>>"))
total = kor+eng+math
avg = (kor+eng+math)/3

print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))
