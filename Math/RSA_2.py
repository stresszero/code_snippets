def RSA_encrypt(plain, e, n):
    encrypted_parts = []
    
    for character in plain:
        ascii_value = ord(character) # 문자를 ASCII 코드로 변환
        encrypted_value = pow(ascii_value, e, n) # RSA 암호화: (ascii_value^e) mod n
        encrypted_parts.append(str(encrypted_value)) # 암호화된 값을 문자열로 변환하여 리스트에 추가
        
    # 공백으로 구분하여 하나의 문자열로 결합
    cipher_text = " ".join(encrypted_parts) 
    return cipher_text


def RSA_decrypt(cipher, d, n):
    decrypted_characters = []
    encrypted_values = cipher.split() # 공백으로 구분된 암호문을 분리
    
    for encrypted_str in encrypted_values:
        encrypted_value = int(encrypted_str) # 문자열을 정수로 변환
        decrypted_value = pow(encrypted_value, d, n) # RSA 복호화: (encrypted_value^d) mod n
        
        original_character = chr(decrypted_value) # 복호화된 값을 문자로 변환
        decrypted_characters.append(original_character) # 복호화된 문자를 리스트에 추가
    
    # 모든 문자를 결합하여 원본 평문 반환
    plain_text = "".join(decrypted_characters)
    return plain_text

p = 43
q = 59
n = p * q  # (소인수 분해가 어렵도록 충분히 큰) 두 소수 p와 q의 곱 
e = 13  # (p-1) * (q-1)과 서로소인 수
public_key = (n, e)  # 공개키
private_key = 937  # 개인키

plain = "plain text"
encrypted = RSA_encrypt(plain, public_key[1], public_key[0])
print(RSA_decrypt(encrypted, private_key, public_key[0]))
