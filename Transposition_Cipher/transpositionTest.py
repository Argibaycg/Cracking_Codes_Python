import random
import sys
import transpositionDecrypt
import transpositionEncrypt


def main():
    random.seed(42)

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)

        random.shuffle(message)

        message = ''.join(message)

        print('Test #%s: "%s...' % (i + 1, message[:50]))

        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encrypt_message(key, message)
            decrypted = transpositionDecrypt.decrypt_message(key, encrypted)

            if message != decrypted:
                print('Mismatch with key %s amd message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('All test has passed')


if __name__ == '__main__':
    main()
