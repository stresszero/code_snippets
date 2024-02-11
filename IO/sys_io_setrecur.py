import sys

input = sys.stdin.readline
print = sys.stdout.write

# 출력할 내용을 문자열로 변환하고 개행을 추가해서 출력해주는 함수
def println(s):
    sys.stdout.write(str(s) + "\n")

# 파이썬의 기본 재귀호출 제한은 1000회이므로 재귀를 활용하여 풀 경우 다음과 같이 설정
sys.setrecursionlimit(10 ** 6)