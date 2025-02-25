# encryption decryption program

import random, string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(f"Chars: {chars}")
print(f"Key  : {key}")

#enc

plain_text = input("Enter any data to be encrypted : ")
ciper_text = " "

for letter in (plain_text):
    index = chars.index(letter)
    ciper_text += key[index]
    # print(index)
print(ciper_text)

inp = input("Do you want to decrypt the text [Y/N]: ")
if inp.lower() == 'y':
    plain_text = " "
    for char in ciper_text:
        # print(char)
        ind = key.index(char)
        # print(ind)
        plain_text += chars[ind]
print(plain_text)