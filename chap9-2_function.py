'''
반환값이 있는 함수
-> 실행 후 결과 값을 남기는 함수
: return 명령어와 반환 값을 열거
  함수 내부에 여러 개의 return 사용 가능 
    첫 번째 return이 나오는 순간, 그 뒤의 코드들은 실행되지 않는다.
'''

# 원뿔 계산 프로그램 개선

def rtn_cone_vol(r,h):
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        return vol
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요.")

print(format(rtn_cone_vol(10,20),">10.3f"))


# 기능 추가하기 *동시 할당

def rtn_cone_vol_surf(r,h):
    if r>0 and h>0: 
        # r,h 모두 양수
        vol = 1/3*3.14*r**2*h
        surf = 3.14*r**2+3.14*r*h
        return vol, surf
    else:
        # r,h 음수
        print("반지름, 높이는 양수를 입력하세요.")

# print(rtn_cone_vol_surf(5,10))
# print(format(rtn_cone_vol_surf(5,10),">20.3f"))
# 위 36번 실행 시 TypeError:unsupported format string passed to tuple.__format__


# 세 개의 사용자 입력을 오름차순으로 정렬하는 함수를 이용하여 정렬된 값을 출력하는 문제
'''  
a = int(input("첫 번쨰 값을 입력하세요:"))
b = int(input("두 번쨰 값을 입력하세요:"))
c = int(input("세 번쨰 값을 입력하세요:"))

def sort3(a,b,c):
    if c>b:
        c,b=b,c
    if c>a:
        c,a=a,c
    if b>a:
        b,a=a,b
    
    print(a,b,c)
    
sort3(a,b,c)
'''

# 변수의 스코프

x=1
print("1. x의 값은",x)

def inc(x):
    x=x+1
    print("2. x의 값은",x)
    
inc(x)
print("3. x의 값은",x)


# 여러 개의 수을 입력받고 합과 평균을 반환하는 var_sum_avg 함수를 사용하여, (20,25,10,85,100,150)에 대한 합과 평균을 출력하시오.

def var_sum_avg(*numbers):
    sum = 0
    count = 0
    
    for i in numbers:
        sum = sum + i
        count = count + 1
        
    return sum, sum/count

print(var_sum_avg(20,25,10,85,100,150)) 