"""
Decoder
Supports: Base64, Caesar Cipher, ROT13, XOR
"""

import base64


def base64_decode(text: str) -> str:
    return base64.b64decode(text.encode()).decode()

def caesar_decode(text: str, shift: int = 3) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def rot13(text: str) -> str:
    return caesar_decode(text, 13)

def xor_decode(hex_text: str, key: str) -> str:
    raw = bytes.fromhex(hex_text)
    key_bytes = key.encode()
    decoded = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(raw))
    return decoded.decode()


if __name__ == "__main__":
    xor_key = "secret"

    print("[Base64]         ", base64_decode("SGVsbG8sIFdvcmxkIQ=="))
    print("[Caesar shift=5] ", caesar_decode("Mjqqt, Btwqi!", shift=5))
    print("[ROT13]          ", rot13("Uryyb, Jbeyq!"))
    print("[XOR key=secret] ", xor_decode("3a0b1e0b531f150f001b18", xor_key))
