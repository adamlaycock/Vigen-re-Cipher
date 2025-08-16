import pandas as pd

ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ')
NUMBERS = list('0123456789')
SYMBOLS = list('!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`£€')
CHARACTERS = ALPHABET + NUMBERS + SYMBOLS
VALID_OPTIONS = ['encryption', 'decryption']

def validate_input(
    text: str
) -> str:
    """
    Checks inputted text for characters that are not present in CHARACTERS. If 
    unsupported characters are found, displays an error and removes them from
    the inputted text.

    Args:
        text (str): String to be assessed for unsupported characters.

    Returns:
        str: String after unsupported characters have been removed.
    """
    invalid = set(text) - set(CHARACTERS)
    if invalid:
        print(f"\nUnsupported character/s found: {' '.join(invalid)}")
        print('Removing unsupported characters from the string.\n')
    text = ''.join(char for char in text if char in CHARACTERS)

    return text

def construct_table(
    table_key: str
) -> pd.DataFrame:
    """
    Constructs a Pandas DataFrame containing a Vigenère table built from a
    custom alphabet using table_key.

    Args:
        table_key (str): String used to build a custom alphabet for the 
                         Vigenère table.

    Returns:
        pd.DataFrame: Pandas DataFrame containing the Vigenère table with 
                      appropriate columns and indices.
    """
    table_key = list(table_key)
    seen = set()
    alphabet = [char for char in table_key + CHARACTERS if not (char in seen or seen.add(char))]

    table = []
    for i in range(len(alphabet)):
        rotated = alphabet[i:] + alphabet[:i]
        table.append(rotated)

    table = pd.DataFrame(table)
    table.columns = alphabet
    table.index = alphabet

    return table


def encrypt_plaintext(
    plaintext: str,
    key: str,
    table_key: str
):
    """
    Encrypts a message through a Vigenère cipher using a cipher key and a key 
    to construct a custom alphabet.

    Args:
        plaintext (str): String containing the message text to be encrypted.
        key (str): Cipher key to use for encryption.
        table_key (str): String used to build a custom alphabet for the 
                         Vigenère table.

    Returns:
        None
    """
    table = construct_table(table_key)

    ext_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    
    cipher_text = []
    for p_char, k_char in zip(plaintext, ext_key):
        cipher_text.append(table.loc[p_char, k_char])

    print(''.join(cipher_text))


def decrypt_ciphertext(
    cipher_text: str,
    key: str,
    table_key: str
):
    """
    Decrypts a message encoded using a Vigenère cipher when provided the 
    cipher key and the key to construct the custom alphabet used for 
    encryption.

    Args:
        cipher_text (str): String containing the encrypted message.
        key (str): Cipher key to use for encryption.
        table_key (str): String used to build a custom alphabet for the 
                         Vigenère table.

    Returns:
        None
    """
    table = construct_table(table_key)

    ext_key = (key * ((len(cipher_text) // len(key)) + 1))[:len(cipher_text)]

    plaintext = []
    for c_char, k_char in zip(cipher_text, ext_key):
        plaintext.append(table[table[k_char] == c_char].index[0])

    print(''.join(plaintext))

def get_valid_choice():
    """
    Prompts the user for information on whether they would like to encrypt or
    decrypt messages using the cipher.

    Args:
        None

    Returns:
        str: String containing either 'encryption' or 'decryption'.
    """
    while True:
        print('Would you like to use encryption or decryption functionality?')
        choice = input(
            'Please choose from either "encryption" or "decryption":'
        )
        choice = choice.strip().lower()

        if choice in VALID_OPTIONS:
            return choice
        
        print(f'Unexpected input: "{choice}".') 
        print('Please choose from either "encryption" or "decryption".\n')

def get_user_inputs():
    """
    Prompts the user to provide information necessary for encryption or 
    decryption.

    Args:
        None

    Returns:
        str: String containing the text after removal of unsupported 
             characters.
        str: String containing the alphabet key after removal of unsupporeted
             characters.
        str: String containing the cipher key after the removal of unsupported
             characters.
    """
    print('TEXT:')
    text = input('Enter text: ').strip()
    text = validate_input(text)
    print(text)

    print('\nCHARACTERS KEY:')
    table_key = input('Enter alphabet key: ').strip()
    table_key = validate_input(table_key)
    print(table_key)

    print('\nCIPHER KEY:')
    key = input('Enter cipher key: ').strip()
    key = validate_input(key)
    print(key)

    return text, table_key, key

def main():
    print('Vigenère Cipher Tool\n')

    choice = get_valid_choice()
    print(f'\nYou have chosen {choice}.\n')

    text, table_key, key = get_user_inputs()

    print('\nOUTPUT:')
    if choice == 'encryption':
        encrypt_plaintext(text, key, table_key)
    else:
        decrypt_ciphertext(text, key, table_key)

if __name__ == '__main__':
    main()
