ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'




def rotate_left(string: str):
    return string[1:] + string[:1]

table_key = 'hello123'

alphabet = list(ALPHABET)
table_key = list(table_key.upper())

custom_alphabet = table_key + [char for char in alphabet if char not in table_key]

print(custom_alphabet)


        

