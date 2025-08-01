table_key = list('hello')

def rotate_left(string: str):
    return string[1:] + string[:1]


def build_table(
    table_key: str,
):
    table = []

