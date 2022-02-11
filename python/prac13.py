# prac13.py
# 13. 사용자에게 20보다 작은 숫자를 입력하라고 요청한다. 만약 입력된 값이 20과
# 같거나 크면 "Too high"를 출력. 아니면 "Thank you" 출력.
num = int(input('enter number under 20 : '))
if num > 20 or num == 20:
	print('Too high')
else:
	print('Thank you')