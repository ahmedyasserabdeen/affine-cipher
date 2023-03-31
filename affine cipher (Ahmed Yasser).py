ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(plaintext, a, b):
    ciphertext = ''
    for char in plaintext.lower():
        if char in ALPHABET:
            idx = ALPHABET.index(char)
            encrypted_idx = (a*idx+b) % 26
            ciphertext += ALPHABET[encrypted_idx]
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext,a,b):
    plaintext = ''
    for char in ciphertext.lower():
        if char in ALPHABET:
            idx=ALPHABET.index(char)
            decrypted_idx=(modinv(a,26)*(idx-b))%26
            plaintext+=ALPHABET[decrypted_idx]
        else:
            plaintext+=char
    return plaintext
def modinv(a,m):
    _, x, _ = extended_euclidean_algorithm(a, m)
    return x % m
def extended_euclidean_algorithm(a,b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y


#message = input('Enter message: ')
a = int(input('Enter key a: '))
b = int(input('Enter key b: '))
mode = input('Enter "e" or "d": ')

if mode == 'e':
    with open('path') as f:
        message = f.readlines()
    for i in range(len(message)):
        ciphertext = encrypt(message[i], a, b)
        with open('path', 'w') as f:
            f.write(ciphertext)
elif mode == 'd':
    with open('path') as f:
        message = f.readlines()
    for i in range(len(message)):
        plaintext = decrypt(message[i], a, b)
        with open('path', 'w') as f:
            f.write(plaintext)
else:
    print('Invalid mode. Enter "encrypt" or "decrypt".')
