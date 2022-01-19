def encrypt_decrypt(text, step, lang, direction):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    encrypt_string = ''

    if lang == 'ru':
        alphas = 32
        low_alpha = rus_lower_alphabet
        upper_alpha = rus_upper_alphabet
    if lang == 'en':
        alphas = 26
        low_alpha = eng_lower_alphabet
        upper_alpha = eng_upper_alphabet

    for i in text:
        if i.isalpha():
            if i == i.lower():
                place = low_alpha.index(i)
            if i == i.upper():
                place = upper_alpha.index(i)

            if direction == 'encrypt':
                index = (place - int(step)) % alphas
            elif direction == 'decrypt':
                index = (place + int(step)) % alphas

            if i == i.lower():
                encrypt_string += low_alpha[index]
            if i == i.upper():
                encrypt_string += upper_alpha[index]

        else:
            encrypt_string += i
    return encrypt_string
