# def encryption_cesar(text, step, lang):
#     encrypt_text = ''
#     if lang == 'ru':
#         for i in text:


def decryption_cesar(text, step, lang):
    dencrypt_text = ''
    if lang == 'en':
        for i in range(len(text)):
            n = ord(text[i]) - step
            if n < 97:
                n = 122 - (96 - n)
            dencrypt_text+=chr(n)
    return dencrypt_text


print(decryption_cesar('bwfusvfupdbftbs', 1, 'en'))