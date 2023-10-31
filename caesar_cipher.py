import string

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key + key) % vocab_size
        encrypted += num_char_map[rotation]
    return encrypted


def decrypt(text, key):
    decrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key - key) % vocab_size
        decrypted += num_char_map[rotation]
    return decrypted


vocab_size = len(string.ascii_lowercase + " ")


key = 3
message = 'Indonesia'

print('message is :', message)

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print('encrypted :', encrypted_message)
print('decrypted :', decrypted_message)