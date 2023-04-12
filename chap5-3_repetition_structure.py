# "저는 파이썬을 잘 다룰 수 있습니다" 를 5번 출력하시오.
sentence = "저는 파이썬을 잘 다룰 수 있습니다."
i = 1  # 반복이 될지 말지 결정하는 변수: 감시 값, 감시자, sentinel

while i < 6:
    print(sentence)
    i = i + 1
# 무한 루프 주의!!!!!!!!!
# 따라서 반복 구조를 사용할 때는 종료가 되는지 꼭 판단할 것!

print("-------")

# n까지 합 계산 프로그램
n = int(input("n 값을 입력하세요: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1
    
print(sum)
    
print("-------")

# 구구단 출력 프로그램
num = int(input("숫자를 입력하세요: "))
x = 1

while x <= 9:
    y = x * num
    print(num, "x", x, "=",y)
    x = x + 1

"""    
또 다른 방법

while x <= 9:
    print(num, "x", x, "=", x * num)
    x = x + 1
   
코드가 더 간단해짐.
즉, 간단하게 만들 수 있으면, 간단하게 만들자!    
"""

## list
# 구문형식
# list([원소1, 원소2, 원소3, 등등]) 또는 [원소1, 원소2, 등등]
# 예시:     [1,4,5,6,9] 또는 make_list = [1,4,5,7,9] 또는 body = [172, 70, "black eyes", "black hair"] 
# 여러개의 원소 타입도 하나의 리스트로 묶을 수 있음


## 인덱스 연산자
# 시퀀스 타입의 원소에 접근하는 연산자
# 원소에 부여된 인덱스 번호로 지칭
# 0부터 시작! 혼동 금지!!!!!!
# 즉, body = [172, 70, "black eyes", "black hair"] 에서  body[0] = 172 body[1] = 70 이렇게



first_list = [1, 3, 5, 7, 9]
print(first_list[4])

for i in first_list:
    print(i)


# 다양한 높이를 가지는 원기둥 계산 프로그램 -> 리스트를 사용할 것!
height_list = [1,5,14,26,31]
radius = int(input("반지름을 입력하세요: "))

for height in height_list:
    area = radius ** 2 * 3.14 + radius * 2 * 3.14 * height
    volume = radius ** 2 * 3.14 * height
    print("겉넓이는", area, "이고", "부피는", volume)
