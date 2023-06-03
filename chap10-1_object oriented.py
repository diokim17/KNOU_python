# 원뿔 부피, 겉넓이 구하기
class Cone:
    def __init__(self,radius=20,height=30):
        self.r=radius
        self.h=height
        
    def get_vol(self):
        return 1/3*3.14*self.r**2*self.h
    
    def get_surf(self):
        return 3.14*self.r**2+3.14*self.r*self.h
        
unit_cone=Cone() # 별도의 값을 지정해주지 않으면 위에서 정의한 값이 들어감
big_cone=Cone(50,100)        

print("부피는",unit_cone.get_vol())
print("겉넓이는",unit_cone.get_surf())

print("부피는",big_cone.get_vol())
print("겉넓이는",big_cone.get_surf())

# BMI 구하기
class BMI:
    def __init__(self,name,age,weight,height):
        self.n=name
        self.a=age
        self.w=weight
        self.h=height
        
    def get_BMI(self):
        self.result=self.w/(self.h/100)**2
        return self.result
    
    def get_status(self):
        if self.result >= 25:
            self.status="비만"
            return self.status
        elif 23 <= self.result < 25:
            self.status="과체중"
            return self.status
        elif 18.5 <= self.result < 23:
            self.status="정상"
            return self.status
        else:
            self.status="저체중"
            return self.status
            
    def print_all(self):
        print(self.n,"님은",self.a,"살 이고, BMI 지수는",self.result,"이고",self.status,"입니다.")
        
    
person1=BMI("홍길동",37,72,172)
# print(person1.get_BMI())
# print(person1.get_status())
person1.get_BMI()
person1.get_status()
print(person1.print_all())