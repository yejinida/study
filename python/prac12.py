# prac12.py
# 12. 두 개의 숫자를 입력받는다. 만약 첫 번째 숫자가 두 번째 숫자보다 크면,
# 두 번째 숫자를 먼저 출력, 그렇지 않다면 첫 번쨰 숫자를 먼저 출력하라.
a, b = map(int, input().split())
if a > b:
	print(str(b) + " " + str(a))
else:
	print(str(a) + " " + str(b))