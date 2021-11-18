# makes plain text into encoded text
import json
import re
from clize import run
from tqdm import tqdm


def ireplace(old, repl, text):
    return re.sub('(?i)'+re.escape(old), lambda m: repl, text)

def main(text: str):
    with open('dictionary.json', 'r') as file:
        dictionary = json.load(file)

    rgx = re.compile("(\b[^\s]+\b)")

    words = rgx.findall(text)
    print(words)
    for word in tqdm(words):
        word = word.lower()
        if word in dictionary:
            text = ireplace(word, f'({dictionary[word][0][0]}:{dictionary[word][0][1]})', text)

    print(text)

if __name__ == '__main__':
    run(main)