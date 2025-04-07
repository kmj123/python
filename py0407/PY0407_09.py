class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no = no
        self.__name = name
        self.__kor = kor # __ 언더바 2개 접근제한: 캡슐화
        self.__eng = eng
        
    def getNo(self): return self.__no
    def getName(self): return self.__name
    
    # getter    / getter, setter 아니면 데이터에 접근을 못하게 막음
    # @어노테이션 @property, @변수,
    @property   #print(Stu.kor)
    def kor(self): 
        return self.__kor
    
    # def kor(self):
    #     self.__kor = KeyError
    
    @kor.setter # s.kor = 90 s.kor = 150 # raise 에러
    def SetKor(self, kor):
        if kor>=0 and kor <= 100:
                self.__kor = kor
        else :
            raise NotImplementedError("유효값이 아닙니다.")
    
    # setter
    def SetKor(self, kor):
        if kor>=0 and kor <= 100:
            self.__kor = kor
        else :
            raise NotImplementedError("유효값이 아닙니다.")
    # getter
    def geEng(self):
        return self.__eng 
    # setter
    def setEng(self,eng):
        if eng>=0 and eng <= 100:
            self.__eng = eng
        else: raise NotImplementedError("유효한 데이터가 아닙니다.")
               
    def __str__(self):
        return f"{self.no},{self.name},{self.__kor},{self.eng}"
    

s = Stu(1,"홍길동",100,99)
s.__kor = 200   #2.kor
print(s.__no,s.__name,s.__kor)    # 지역변수개념의 s.__kor 의 값 출력
s.eng = 300
s.SetKor(500)
print(s)