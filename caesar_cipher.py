letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = (index + key) % num_letters
                result += letters[new_index]
        else:
            result += ' '  # Preserve spaces
    return result

def main():
    print('*** CAESAR CIPHER ***')
    print()

    while True:
        print('Do you want to Encrypt, Decrypt, or Quit?')
        user_input = input('e/d/q: ').lower()
        print()

        if user_input == 'e':
            print('ENCRYPTION MODE SELECTED')
            print()
            key = int(input('Enter the key (1 through 26): '))
            text = input('Enter the text to encrypt: ')
            ciphertext = encrypt_decrypt(text, user_input, key)
            print(f'CIPHERTEXT: {ciphertext}')
            print()
        elif user_input == 'd':
            print('DECRYPTION MODE SELECTED')
            print()
            key = int(input('Enter the key (1 through 26): '))
            text = input('Enter the text to decrypt: ')
            plaintext = encrypt_decrypt(text, user_input, key)
            print(f'PLAINTEXT: {plaintext}')
            print()
        elif user_input == 'q':
            print('Exiting program...')
            break
        else:
            print('Invalid choice. Please enter e, d, or q.')
            print()

if __name__ == "__main__":
    main()
