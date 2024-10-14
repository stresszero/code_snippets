def RSA_encrypt(plain, e, n):
    return " ".join(str(pow(ord(c), e, n)) for c in plain)


def RSA_decrypt(cipher, d, n):
    return "".join(chr(pow(int(c), d, n)) for c in cipher.split())

n = 2537  # (소인수 분해가 어렵도록 충분히 큰) 두 소수의 곱 (43 * 59)
e = 13  # (p-1) * (q-1)과 서로소인 수
public_key = (n, e)  # 공개키
private_key = 937  # 개인키

plain = "plain text"
encrypted = RSA_encrypt(plain, public_key[1], public_key[0])
print(RSA_decrypt(encrypted, private_key, public_key[0]))
