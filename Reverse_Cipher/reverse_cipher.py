# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licenced)

message = input('Shh, what do you want to hide?:')
translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print('It\'s secret now: ', translated)
