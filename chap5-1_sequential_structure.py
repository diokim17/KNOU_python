# 순차구조로 삼각형 출력하기
print("  *")
print(" ***")
print("*****")

# input 함수, 사용자의 입력을 받아드림
# value = input("값을 입력하세요: ")

# 사용자에게 값을 입력받아 삼각형 넓이를 계산하는 프로그램 만들어보기
base = int(input("밑변을 입력하세요: "))
height = int(input("높이를 입력하세요: "))
area = base * height / 2

print("넓이는", area)