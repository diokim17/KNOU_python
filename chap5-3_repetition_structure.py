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

# 다양한 높이를 가지는 원뿔 계산 프로그램 -> 리스트를 사용할 것!
