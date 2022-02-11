# prac11.py
# 11. 사용자로부터 100이 넘는 숫자를 입력받고 10미만의 숫자 하나를 입력받은 후,
# 작은 숫자가 큰 숫자 안에 몇 번 들어가는지 구하여라
big_num, small_num = map(int, input().split())
print(big_num // small_num)