from caesar.encrypt import caesar_encrypt
from caesar.decrypt import caesar_decrypt

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid option! Please choose 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (0-25): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'encrypt':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
