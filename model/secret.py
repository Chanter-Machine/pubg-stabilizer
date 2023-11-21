import datetime
import os

import random
import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
from cryptography.hazmat.primitives import serialization


def encrypt_aes(key, data):
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)

    # Use AES algorithm with CBC mode and PKCS7 padding
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the data using PKCS7
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data.encode('utf-8')) + padder.finalize()

    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and ciphertext and return Base64 encoded result
    result = iv + ciphertext
    return base64.b64encode(result).decode('utf-8')


def decrypt_aes(key, ciphertext):
    # Decode Base64 and extract IV
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Use AES algorithm with CBC mode and PKCS7 padding
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the data using PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode('utf-8')


def read_pem_file(file_path, password=None):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:  # Make sure there is at least two lines
            decoded_bytes = base64.b64decode(lines[1])
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string


def generate_aes_key(input_string):
    # Convert the input string to bytes
    input_bytes = input_string.encode('utf-8')

    if len(input_bytes) > 32:
        raise ValueError("Input string must be 32 bytes or less")

    remaining_bytes = 32 - len(input_bytes)

    # 使用 random.choices 从字符集中随机选择字符，构成指定长度的字符串
    random_string = ''.join(
        random.sample('zyxwvutsrqponmlkjihgfedcba1234567890{}[]./*-<>?!@#$%^&*()_+-=', remaining_bytes))

    return input_string + random_string


# 示例用法
# pem_file_path = "../resource/secrets/key.pem"
# private_key = read_pem_file(pem_file_path, None)
# print(private_key)

# Example usage
# key = os.urandom(32)  # 256 bits key for AES-256
# key = "yChAoyuNo1.$"
# newKey = generate_aes_key(key)
# newKeyLen = len(newKey)
# print(newKey)
# print(newKeyLen)
# data = 'Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!Hello, AES!'

# Encrypt
# encrypted_data = encrypt_aes(newKey.encode(), data)
# print("Encrypted:", encrypted_data)
#
# # Decrypt
# decrypted_data = decrypt_aes(newKey.encode(), encrypted_data)
# print("Decrypted:", decrypted_data)


def generate_secrets_test(file_path: str):
    texts = ["-----BEGIN PRIVATE KEY-----"]

    def days_later(days=0):
        # Get the current date
        current_date = datetime.datetime.now()

        # Calculate the date five days later
        date_after_five_days = current_date + datetime.timedelta(days)

        # Return the date in 'yyyy-mm-dd' format
        return date_after_five_days.strftime('%Y-%m-%d')

    def generate_line(ori_line):
        # Convert the string to bytes, then encode it with Base64
        rest_len = 64 - len(ori_line)
        random_string = "".join(random.choices(string.ascii_letters + string.digits, k=rest_len))
        encoded_string = base64.b64encode(ori_line.encode() + random_string.encode('utf-8'))

        # Decode the byte string to normal string
        return encoded_string.decode('utf-8')

    for _ in range(6):  # Generate 10 lines
        line = generate_line("")
        texts.append(line)
    validate_until = days_later(3)
    special_line = generate_line(validate_until)
    texts.append(special_line)
    for _ in range(6):  # Generate 10 lines
        line = generate_line("")
        texts.append(line)
    texts.append("-----END PRIVATE KEY-----")
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write each element of the list to a new line of the file
        for item in texts:
            file.write("%s\n" % item)

def parse_activate(file_path: str) -> str:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:  # Make sure there is at least two lines
            decoded_bytes = base64.b64decode(lines[7])
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string[:10]


if __name__ == '__main__':
    generate_secrets_test("../resource/secrets/activate")
    print(parse_activate("../resource/secrets/activate"))
