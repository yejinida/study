# prac14.py
# 14. 사용자에서 10 < 숫자 <= 20 숫자를 입력 받고 이 범위 안이면 땡큐
num = int(input())
if num > 10 and (num < 20 or num == 20):
	print('Thank you')
else :
	print('Incorrect answer')
