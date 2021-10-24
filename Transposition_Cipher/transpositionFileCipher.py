import os
import sys
import time
import transpositionDecrypt
import transpositionEncrypt


def main():
    input_filename = 'tirso.txt'
    output_filename = 'encrypted.tirso.txt'

    my_key = 10
    my_mode = 'encrypt'

    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % input_filename)
        sys.exit()

    if os.path.exists(input_filename):
        print('This will overwrite the file %s. (C)Continue or (Q)Quit?' % output_filename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print('%sing...' % (my_mode.title()))

    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transpositionEncrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transpositionDecrypt.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print('%sion time: %s seconds' % (my_mode.title(), total_time))

    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(translated)
    output_file_obj.close()

    print('Done %sing %s (%s characters).' % (my_mode, input_filename, len(content)))
    print('%sed file is %s.' % (my_mode.title(), output_filename))


if __name__ == '__main__':
    main()
