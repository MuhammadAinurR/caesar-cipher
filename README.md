# What is the Caesar cipher?

The Caesar cipher is a simple substitution cipher that encrypts plaintext by shifting each letter by a certain number of positions. It is one of the oldest and simplest encryption methods known, and it is named after Julius Caesar, who is said to have used it to encrypt his military messages.

# How does the Caesar cipher work?

The Caesar cipher uses a key, which is the number of positions by which each letter is shifted. To encrypt a message, each letter is replaced by the letter that is a certain number of positions further down the alphabet. For example, with a key of 3, the letter "A" would be replaced by the letter "D".

To decrypt a message, the reverse process is performed. Each letter is replaced by the letter that is a certain number of positions further up the alphabet. For example, with a key of 3, the letter "D" would be replaced by the letter "A".

# What is a message?

A message is the text or data that is to be encrypted or decrypted. It is also referred to as the plaintext or ciphertext, depending on whether it has been encrypted or decrypted.

# What is a key?

A key is a secret piece of information that is used to encrypt or decrypt a message. In the case of the Caesar cipher, the key is a number that represents the number of positions by which each letter is shifted.

# Conclusion

The Caesar cipher is a simple but effective substitution cipher. It is easy to implement and use, and it can be used to encrypt and decrypt messages of any length. However, it is also a relatively easy cipher to break, so it is not recommended for use with sensitive data.

# How to use this source code

This source code provides a simple implementation of the Caesar cipher in Python. To use it, simply run the program and dont forget to configure message and key in the file. The program will then encrypt or decrypt the message.

# code explanation

It works by creating two dictionaries: **char_num_map** and **num_char_map**. The **char_num_map** dictionary maps each character in the alphabet (plus the space character) to a number, and the **num_char_map** dictionary maps each number to a character.

The **encrypt()** function encrypts a message using the Caesar cipher. It takes a message and a key as input and returns an encrypted message. The key determines how many positions each letter in the message is shifted. For example, with a key of 3, the letter "A" would be shifted to the letter "D".

The **decrypt()** function decrypts a message encrypted with the Caesar cipher. It takes an encrypted message and a key as input and returns the original message. The key is the same key that was used to encrypt the message.

Here is a step-by-step explanation of the code:

1. Import the **string** module. The **string** module contains a number of useful functions and constants for working with strings.
2. Create two dictionaries: **char_num_map** and **num_char_map**. The **char_num_map** dictionary maps each character in the alphabet (plus the space character) to a number, and the **num_char_map** dictionary maps each number to a character.
3. Define the **encrypt()** function. This function encrypts a message using the Caesar cipher. It takes a message and a key as input and returns an encrypted message.
4. Define the **decrypt()** function. This function decrypts a message encrypted with the Caesar cipher. It takes an encrypted message and a key as input and returns the original message.
5. Set the key to 3.
6. Set the message to the string "Indonesia".
7. Print the message to the console.
8. Encrypt the message using the **encrypt()** function.
9. Decrypt the encrypted message using the **decrypt()** function.
10. Print the encrypted and decrypted messages to the console.

# Output Example
![img1](https://github.com/MuhammadAinurR/caesar-cipher/blob/main/output-caesar/output1.png)
![img2](https://github.com/MuhammadAinurR/caesar-cipher/blob/main/output-caesar/output2.png)
