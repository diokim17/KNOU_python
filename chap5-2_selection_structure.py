print(3>6)
print(3<6)
print(3==6)

a = 10
b = 20
c = a == b
print(a==b)
print(c)

print("-------")

temp = 20
fruit = "apple"

# 두 조건이 모두 참이어야 참 출력
print(temp <= 27 and fruit == "banana")

# 두 조건 중 하나라도 참이면 참 출력
print(temp <= 27 or fruit == "banana")

print("-------")

# 삼각형 넓이 구하는 프로그램 개선
base = int(input("밑변을 입력하세요: "))
height = int(input("높이를 입력하세요: "))
area = base * height / 2

# 밑변과 높이가 양수일 때만 실행
if base > 0 and height > 0:
    print("넓이는", area)
else:
    print("올바른 값이 아닙니다.")


print("-------")
    
# 3개의 수를 입력받고 가장 큰 수를 찾는 프로그램 만들기
number1 = int(input("첫 번째 숫자를 입력하세요: "))
number2 = int(input("두 번째 숫자를 입력하세요: "))
number3 = int(input("세 번째 숫자를 입력하세요: "))

if number1 > number2 and number1 > number3:
    print("가장 큰 수는", number1)
elif number2 > number1 and number2 > number3:
    print("가장 큰 수는", number2)
elif number1 == number2 == number3:
    print("모두 같은 수 입니다.")
else:
    print("가장 큰 수는", number3)

# 중첩 선택 구조를 이용해 위의 코드를 변경해보기
if number1 > number2:
    if number1 > number3:
        print("가장 큰 수는", number1)
    else:
        print("가장 큰 수는", number3)
elif number1 == number2 == number3:
    print("모두 같은 수 입니다.")
else:
    if number2 > number3:
        print("가장 큰 수는", number2)
    else:
        print("가장 큰 수는", number3)
        
        
print("-------")

# 내장 함수를 이용해서 가장 큰 수 찾기
print(max(number1,number2,number3))
            
        
            