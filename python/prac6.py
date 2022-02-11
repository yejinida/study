# prac6.py
# 6. 사용자로부터 처음에 가지고 있었던 피자 조각 수를 입력받고, 몇 조각을 먹었는지
# 입력받아서 남은 조각 수를 계산하여 사람에게 익숙한 형식으로 출력하라.
pizza = int(input('pizza : '))
ate = int(input('ate : '))
print('total : ' + str(pizza - ate)) 