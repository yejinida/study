# prac8.py
# 8. 계산서의 총 가격과 몇 명이 같이 식사를 했는지 입력받는다. 총 가격을
# 인원수로 나누고 각 사람이 얼마씩 내야 하는지 출력하라.
tot, people_num = map(int, input().split())
print('dutchpay : ' + str(tot // people_num)) 
