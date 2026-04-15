"""
Encoder
Supports: Base64, Caesar Cipher, ROT13, XOR
"""

import base64


def base64_encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def caesar_encode(text: str, shift: int = 3) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def rot13(text: str) -> str:
    return caesar_encode(text, 13)

def xor_encode(text: str, key: str) -> str:
    key_bytes = key.encode()
    encoded = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text.encode()))
    return encoded.hex()


if __name__ == "__main__":
    message = "Hello, World!"
    xor_key = "secret"

    print(f"Original : {message}\n")
    print(f"[Base64]         {base64_encode(message)}")
    print(f"[Caesar shift=5] {caesar_encode(message, shift=5)}")
    print(f"[ROT13]          {rot13(message)}")
    print(f"[XOR key=secret] {xor_encode(message, xor_key)}")
