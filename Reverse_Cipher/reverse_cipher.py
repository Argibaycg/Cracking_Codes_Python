# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licenced)

message = 'This is the message that you want to cipher'
translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
