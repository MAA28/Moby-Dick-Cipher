# makes plain text into encoded text
import json
import re
from clize import run
from tqdm import tqdm
from random import choice


def encrypt(file_name: str, plain_text: str) -> str:
    f"""
    Encrypts the text using the data from "{file_name} dictionary.json".
    :param file_name: 
    :param plain_text:
    :return encrypted_text:
    """
    with open(f'{file_name.split(".")[0]} dictionary.json', 'r') as file:
        dictionary = json.load(file)

    rgx = re.compile(r'\b[^\s]+\b')

    matches = rgx.finditer(plain_text)

    encoded_text = plain_text
    for match in tqdm(matches):
        if match.group(0).lower() in dictionary:
            replacement = choice(dictionary[match.group(0).lower()])
            encoded_text = encoded_text.replace(match.group(0), f'({replacement[0]}:{replacement[1]})', 1)

    return encoded_text


def main(file_name: str, text: str):
    print(encrypt(file_name,text))


if __name__ == '__main__':
    run(main)
