import pandas as pd

ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def rotate_left(alphabet_list: list):
    return alphabet_list[1:] + alphabet_list[:1]

table_key = 'hello123'
table_key = list(table_key.upper())

alphabet = list(set(table_key + [char for char in ALPHABET if char not in table_key]))

table = []
for i in range(len(alphabet) - 1):
    if i != 0:
        alphabet = rotate_left(alphabet)
        table.append(alphabet)
    else:
        table.append(alphabet)

table = pd.DataFrame(table)
table.columns = ALPHABET
table.index = ALPHABET


