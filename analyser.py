import re
from tqdm import tqdm
import json


def analyser(file_name: str):
    with open(file_name, 'r') as file:
        moby_dick = file.read()

    chapters_array = moby_dick.split('CHAPTER ')
    chapters = {}
    rgx = re.compile(r"(\b[^\s]+\b)")

    for chapter in tqdm(chapters_array, desc=f'Analysing {file_name} for chapters'):
        lines = chapter.split('\n')
        title = ' '.join(lines[0].split(' ')[1:])
        content = '\n'.join(lines[1:])
        chapters[title] = [content[match.start():match.end()] for match in rgx.finditer(content)]

    with open(f'{file_name.split(".")[0]} chapters.json', 'w') as file:
        json.dump(chapters, file, indent=4)

    dictionary = {}

    for i, title in enumerate(tqdm(chapters, desc=f'Analysing {file_name} for words')):
        words = chapters[title]
        for j, word in enumerate(words):
            word = word.lower()
            if word not in dictionary:
                dictionary[word] = [(i, j)]
            else:
                dictionary[word].append((i, j))

    with open(f'{file_name.split(".")[0]} dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=4)


if __name__ == '__main__':
    analyser('moby dick.txt')
