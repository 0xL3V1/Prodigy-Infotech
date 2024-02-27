def caesar_cipher(text, shift, direction):

    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            cipher_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += cipher_char if direction == 'encrypt' else chr(
                (ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result


direction = input("Do you want to encrypt or decrypt the text? (encrypt/decrypt): ")
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
print(f"The {direction}ed text is: {caesar_cipher(text, shift, direction)}")