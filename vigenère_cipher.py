import pandas as pd

ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def construct_table(
    table_key: str
) -> pd.DataFrame:
    
    table_key = list(table_key.upper())
    seen = set()
    alphabet = [char for char in table_key + ALPHABET if not (char in seen or seen.add(char))]

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
    
    table = construct_table(table_key)

    plaintext = plaintext.upper()
    key = key.upper()
    ext_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    
    cipher_text = []
    for p_char, k_char in zip(plaintext, ext_key):
        cipher_text.append(table.loc[p_char, k_char])

    print(''.join(cipher_text))


def decrypt_plaintext(
    cipher_text: str,
    key: str,
    table_key: str
):
    table = construct_table(table_key)

    cipher_text = cipher_text.upper()
    key = key.upper()
    ext_key = (key * ((len(cipher_text) // len(key)) + 1))[:len(cipher_text)]

    plaintext = []
    for c_char, k_char in zip(cipher_text, ext_key):
        plaintext.append(table[table[k_char] == c_char].index[0])

    print(''.join(plaintext))
