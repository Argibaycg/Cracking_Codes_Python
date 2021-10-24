# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licenced)

import math


def main():
    my_message = "Cenoonommstmme oo snnio s s c"
    my_key = 8

    plaintext = decrypt_message(my_key, my_message)

    print(plaintext + "|")


def decrypt_message(key, message):
    number_of_columns = int(math.ceil(len(message)/float(key)))

    number_of_rows = key

    number_of_shaded_boxes = (number_of_columns * number_of_rows) - len(message)

    plaintext = [''] * number_of_columns

    column, row = 0, 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == number_of_columns) or\
                (column == number_of_columns - 1 and row >= number_of_rows - number_of_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()
