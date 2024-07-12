import sys

# 파이썬의 기본 재귀호출 제한은 1000회이므로 이 제한을 넘어야 할 경우 다음과 같이 설정
sys.setrecursionlimit(10 ** 6)

# sys.stdin.readline()
# 개행문자(\n)를 포함한 문자열 한 줄만 입력됨
foo = sys.stdin.readline()
print(foo)

# sys.stdin.readlines()
# EOF(^Z, Ctrl+Z)가 입력될 때까지 입력을 받고
# 한 줄씩 개행문자(\n)를 포함한 문자열들이 담긴 리스트를 반환함
bar = sys.stdin.readlines()
for i in bar:
    print(i)

# sys.stdin.read()
# EOF(^Z, Ctrl+Z)가 입력될 때까지 입력을 받아서 개행문자(\n)를 포함한 문자열을 반환함
baz = sys.stdin.read()
print(baz)

# sys.stdout.write()
# 하나의 문자열을 출력한 후에 문자열의 길이를 반환함
# 줄바꿈 하려면 개행문자(\n) 필요
sys.stdout.write("Hello ")
sys.stdout.write("World" + "\n")

# sys.stdout.writelines()
# 하나의 문자열 또는 여러 개의 문자열을 하나로 만들어 출력하고 None을 반환함
sys.stdout.writelines(["Hello ", "World"])

# 빌트인 함수 input, print 대체
input = sys.stdin.readline
print = sys.stdout.write

# 출력할 내용을 문자열로 변환하고 개행을 추가해서 출력해주는 함수
def println(s):
    sys.stdout.write(str(s) + "\n")

