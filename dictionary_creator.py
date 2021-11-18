import re
from tqdm import tqdm
import json

def main():
    with open('moby dick.txt', 'r') as file:
        moby_dick = file.read()

    chapters_array = moby_dick.split('CHAPTER ')
    chapters = {}
    rgx = r"(\b[^\s]+\b)"

    for chapter in tqdm(chapters_array, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
        lines = chapter.split('\n')
        title = ' '.join(lines[0].split(' ')[1:])
        content = '\n'.join(lines[1:])
        #print(content)
        chapters[title] = [content[match.start():match.end()] for match in list(re.finditer(rgx, content, re.MULTILINE))]


    with open('chapters.json', 'w') as file:
        json.dump(chapters, file, indent=4)

    dictionary = {}

    for i, title in enumerate((chapters)):
        words = chapters[title]
        for j, word in enumerate((words)):
            word = word.lower()
            if word not in dictionary:
                dictionary[word] = [(i, j)]
            else:
                dictionary[word].append((i, j))

    print("Saving...")
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=4)

if __name__ == '__main__':
    main()
