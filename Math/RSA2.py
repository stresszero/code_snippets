from sympy import mod_inverse

# 주어진 공개키 (n, e)
n = 2537
e = 13

# 개인키 d 계산
p = 43
q = 59
phi_n = (p - 1) * (q - 1)
# d = mod_inverse(e, phi_n)
d = 937


def encrypt(plain_text, n, e):
    cipher_text = []
    for char in plain_text:
        m = ord(char)
        c = pow(m, e, n)
        cipher_text.append(c)
    return cipher_text


def decrypt(cipher_text, n, d):
    plain_text = ""
    for c in cipher_text:
        m = pow(c, d, n)
        plain_text += chr(m)
    return plain_text


# 예제 평문
plain_text = "Hello, world!"

# 암호화
cipher_text = encrypt(plain_text, n, e)
print("Cipher Text:", cipher_text)

# 복호화
decrypted_text = decrypt(cipher_text, n, d)
print("Decrypted Text:", decrypted_text)
