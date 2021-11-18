# make encoded text into plain text
from clize import run
import json
import re
from tqdm import tqdm


def main(text: str):
    with open('chapters.json', 'r') as file:
        chapters = json.load(file)

    regex = r"([\w][\w']*\w)|\(\d+:\d+\)"

    matches = re.finditer(regex, text, re.MULTILINE)
    words = [text[match.start():match.end()] for match in list(matches)]

    for word in tqdm(words):
        if re.match(r'\(\d+:\d+\)', word):
            i,j = [int(index) for index in word[1:-1].split(':')]
            key = list(chapters.keys())[i]
            content = chapters[key][j]
            text = text.replace(word, content)

    print(text)

if __name__ == '__main__':
    run(main)
