from PIL import Image

def xor_cypher(input_data, key):
    return bytearray(a ^ key for a in input_data)

def encrypt_image(file_path, key):
    img = Image.open(file_path)
    byte_arr = bytearray(img.tobytes())
    encrypted_data = xor_cypher(byte_arr, key)
    encrypted_img = Image.frombytes(img.mode, img.size, bytes(encrypted_data))
    encrypted_img.save('encrypted_image.png')

def decrypt_image(file_path, key):
    img = Image.open(file_path)
    byte_arr = bytearray(img.tobytes())
    decrypted_data = xor_cypher(byte_arr, key)
    decrypted_img = Image.frombytes(img.mode, img.size, bytes(decrypted_data))
    decrypted_img.save('decrypted_image.jpg')


operation = input("Do you want to encrypt or decrypt the image? Enter 'encrypt' or 'decrypt': ")
file_path = input("Enter the file path of the image: ")
key = int(input("Enter the secret key (an integer from (0:255)): "))

if operation.lower() == 'encrypt':
    encrypt_image(file_path, key)
    print("Image encrypted successfully!")
elif operation.lower() == 'decrypt':
    decrypt_image(file_path, key)
    print("Image decrypted successfully!")
else:
    print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")