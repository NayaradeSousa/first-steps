""" Julio Cesar's Cryptography
"""
import requests
import json
import hashlib


def get_data():
    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token'
                            '=SEUTOKEN')
    return response.json()


def send_data():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token' \
          '=SEUTOKEN'
    files = {'answer': ('answer', open('answer.json', 'rb'), 'application/json')}

    r = requests.post(url, files=files)
    print(r.json())


def generates_file(data):
    with open('answer.json', 'w') as answer:
        json.dump(data, answer)


def decipher_cod(desloc, text):
    decipher_text = ''
    for letter in text:
        if not letter.isalpha():
            decipher_text += letter
        else:
            new_letter = chr(ord(letter) - desloc)
            decipher_text += new_letter
    return decipher_text


if __name__ == '__main__':
    response = get_data()
    generates_file(response)
    decrypt_text = decipher_cod(response['numero_casas'], response['cifrado'])
    response['decifrado'] = decrypt_text
    sha1 = hashlib.sha1()
    sha1.update(str(decrypt_text).encode('utf-8'))
    encrypted_text = sha1.hexdigest()
    response['resumo_criptografico'] = encrypted_text
    print(response)
    generates_file(response)
    send_data()
