number = int(input("Enter a number: "))
base = int(input("Enter base: "))
digits = "0123456789abcdef"
result = ""

while number > 0:
    result = digits[number % base] + result
    number //= base

print(result)