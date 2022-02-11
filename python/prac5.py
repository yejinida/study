# prac5.py
# 5. 사용자로부터 3개의 숫자를 입력받는다. 첫 번쨰 숫자와 두 번쨰 숫자를 더한 값에
# 세 번째 숫자를 곱한 결과를 다음과 같이 출력하라.
a, b, c = map(int, input().split())
print('The answer is ' + str(a * b * c))
