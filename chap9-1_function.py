'''
함수
특정 작업을 수행하는 명령문의 집합
'''

# 원뿔 부피 계산 프로그램 개선

def prt_cone_vol(r,h):
    if r > 0 and h > 0 :
        vol = 1/3 * 3.14 * r ** 2 * h
        print("원뿔의 부피:",vol,"입니다.")
    else:
        print("반지름과 높이 값에 양수를 입력하세요.")
        
rad = 20
hei = 30

prt_cone_vol(rad,hei)


# 숫자를 입력받고 역순으로 출력하는 프로그램

def reverse_number(num):
    while num != 0:
        digit = num % 10
        num = num // 10
        print(digit,end="")
        

number = 34567
reverse_number(number)