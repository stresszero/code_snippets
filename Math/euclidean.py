# 유클리드 호제법
def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a
