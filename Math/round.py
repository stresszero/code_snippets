# 파이썬 내장함수 round()는 오사오입(rounding half to even) 방식
# 5미만은 내림, 5초과는 올림, 5인 경우 앞자리가 짝수면 내리고 홀수면 올림
print(round(0.5)) # 0
print(round(1.5)) # 2
print(round(2.5)) # 2
print(round(3.5)) # 4

# 음수인 경우 절대값을 round()한 값에 음수를 붙이는 방식
print(round(-0.5)) # 0
print(round(-1.5)) # -2
print(round(-2.5)) # -2
print(round(-3.5)) # -4

# 사사오입(rounding half up: 5이상 올림, 5미만 내림) 구현
def rounding_half_up(num):
    if num < 0:
        return -rounding_half_up(-num)
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)

# deicmal 모듈 사용
from decimal import Decimal, ROUND_HALF_UP

def custom_round(num):
    return Decimal(num).quantize(Decimal('1'), rounding=ROUND_HALF_UP)