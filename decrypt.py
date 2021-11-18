from clize import run
import json
import re
from tqdm import tqdm


def decrypt(file_name: str, coded_text: str) -> str:
    f"""
    Decrypt coded text using the data from "{file_name} chapters.json".
    :param file_name: 
    :param coded_text:
    :return decrypted_text:
    """
    with open(f'{file_name.split(".")[0]} chapters.json', 'r') as file:
        chapters = json.load(file)

    rgx = re.compile(r"\(\d+:\d+\)")

    matches = rgx.finditer(coded_text)

    encrypted_text = coded_text

    for match in tqdm(matches):
        i, j = [int(index) for index in match.group(0)[1:-1].split(':')]
        key = list(chapters.keys())[i]
        content = chapters[key][j]
        encrypted_text = encrypted_text.replace(match.group(0), content, 1)

    return encrypted_text


def main(file_name: str, text: str):
    f"""
    Decrypt coded text using the data from "{file_name} chapters.json".
    :param file_name: 
    :param text:
    :return decrypted_text:
    """
    print(decrypt(file_name, text))


if __name__ == '__main__':
    run(main)
