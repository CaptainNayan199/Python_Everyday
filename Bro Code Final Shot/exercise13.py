# encryption decryption program

import random, string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
print(f"Chars: {chars}")
print(f"Key  : {key}")
# random.shuffle(key)