# prac9.py
# 9. 사용자로부터 일수(날짜 수)를 입력 받아서 그 일수까지 몇 시간, 몇 분, 몇 초가 
# 남았는지 출력하라

date = int(input())
hour = date * 24
minute = hour * 60
sec = minute * 60
print(str(hour) + 'hours ' + str(minute) + ',minutes ' + str(sec) + ',seconds')



