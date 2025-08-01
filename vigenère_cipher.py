import pandas as pd

ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
table_key = 'hello123'
key = 'lucifer'
plaintext = 'thisisasecretmessage'

def construct_table(table_key: str):
    table_key = list(table_key.upper())
    seen = set()
    alphabet = [c for c in table_key + ALPHABET if not (c in seen or seen.add(c))]

    table = []
    for i in range(len(alphabet)):
        rotated = alphabet[i:] + alphabet[:i]
        table.append(rotated)

    df = pd.DataFrame(table)
    df.columns = alphabet
    df.index = alphabet
    return df

def encrypt_plaintext(
    plaintext: str,
    key: str,
    table: pd.DataFrame
) -> str:
    plaintext = plaintext.upper()
    key = key.upper()
    ext_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    
    cipher_text = []
    for p_char, k_char in zip(plaintext, ext_key):
        cipher_text.append(table.loc[p_char, k_char])
    return ''.join(cipher_text)

table = construct_table(table_key)
encrypted = encrypt_plaintext(plaintext, key, table)
print(encrypted)
