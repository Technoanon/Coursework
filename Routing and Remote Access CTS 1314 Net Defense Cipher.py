# Richard Bruno
# Professor Hopkins
# CTS 23324
# October 27, 2024

# Lesson 6 Discussion
# Programming Caesar Cipher

def caesar_cipher(text, shift_value):
    result = ""
    for char in text:
        if char.isalpha():
            shift_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_offset + shift_value) % 26 + shift_offset)
        else:
            result += char
    return result

# ****Break Down of the Caesar Cipher Program****

# 1. Function Definition
# < def caesar_cipher(text, shift_value): >
# def: This keyword defines a function.
# caesar_cipher: The name of the function.
# text: The parameter that takes the input string (plaintext or ciphertext).
# shift_value: The parameter that takes the integer value used to shift characters.

# 2. Initializing Result
# < result = "" >
# result: An empty string initialized to store the final encrypted or decrypted text.
#

# 3. Iterating Through Each Character
# < for char in text: >
# for char in text: This loop iterates through each character in the input string text.

# 4. Checking if Character is Alphabetic
# <  if char.isalpha(): >
# if char.isalpha(): Checks if the character char is an alphabetic letter (A-Z, a-z).

#  5. Determining ASCII Offset
# < shift_offset = 65 if char.isupper() else 97 >
# shift_offset: Sets the ASCII offset to 65 if the character is uppercase (A-Z),
# or 97 if the character is lowercase (a-z). This helps to wrap around the alphabet correctly.
# **** ASCII Values*****
# Uppercase Letters (A-Z): ASCII values range from 65 to 90.
# Lowercase Letters (a-z): ASCII values range from 97 to 122.

# 6. Shifting Characters
# < result += chr((ord(char) - shift_offset + shift_value) % 26 + shift_offset) >
# ord(char): Converts the character char to its ASCII integer value.
# ord(char) - shift_offset: Normalizes the character to a zero-based index (0-25 for A-Z or a-z).
# + shift_value: Applies the shift to the normalized value.
# % 26: Wraps around the alphabet using Modulo Operation.
# + shift_offset: Converts the normalized value back to the original character range.
# chr(...): Converts the shifted ASCII value back to a character.
# result +=: Appends the shifted character to the result string.

# 7. Non-Alphabetic Characters
#  < else:
#        result += char >
# else: If the character char is not alphabetic, it is added to result unchanged.

# 8. Returning the Result
# < return result >
# return result: Returns the final encrypted or decrypted text stored in result.

# *****Example*****
plaintext = "Hello World"
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)
print("Encrypted:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print("Decrypted:", decrypted_text)
# Renamed the variable shift outside the function to shift_amount to avoid shadowing and ensure clarity.
plaintext = "Khoor Zroug"
shift_amount = 3
decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print("Decrypted:", decrypted_text)
# check decrypt.