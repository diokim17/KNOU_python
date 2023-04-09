# 5/2
print(5/2)

# 소숫점 이하는 버리기 즉, 정수 부분만
print(5//2)

# 나머지 구하기
print(25%7)
print(8.4%0.9)
"""
%를 모듈로 연산자라고 함.

어떤 경우에 사용하는가?

number = 10
number % 2
print(number)
결과: 0   즉, number는 짝수

number = 9
number % 2
print(number)
결과: 1   즉, number는 홀수

프로그램을 짜다 보면 짝수와 홀수에 따라서 서로 다른 실행을 해야하는 경우가 있음.
이렇게 홀수와 짝수를 구별하는 데에 유용하게 쓰임.
"""

# 내장 함수
print(max(1,2,3)) # 최댓값 출력
print(min(1,2,3)) # 최솟값 출력
print(round(3.14)) # 반올림
print(abs(-3)) # 절댓값
print(pow(2,3)) # 거듭제곱, 밑=2, 지수=3 따라서 결과: 8