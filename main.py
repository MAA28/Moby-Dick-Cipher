from decrypt import decrypt
from encrypt import encrypt
from analyser import analyser
from sys import argv


def main():
    if len(argv) == 1 or argv[1] == 'help':
        print("""commands:
    help -> prints this
    analyse <file name of a book> -> analyses the book to make it compatible with this program
    encrypt <file name of a book> <file name of the plain text> [file name, where the result will be saved] -> encrypts a file and saves the result or prints out the result
    encrypt <file name of a book> <file name of the plain text> [file name, where the result will be saved] -> decrypts a file and saves the result or prints out the result

Book format must be like:

CHAPTER 1. Loomings.
Call me Ishmael. Some years ago-never mind how long precisely-having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off-then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.

CHAPTER <n>. <title>
<content>""")
    elif argv[1] == 'analyse':
        analyser(argv[2])
    elif argv[1] == 'decrypt':
        with open(argv[3], 'r') as file:
            text = file.read()

        result = decrypt(argv[2], text)

        if len(argv) == 3:
            with open(argv[4], 'w') as file:
                file.write(result)
        else:
            print(result)

    elif argv[1] == 'encrypt':
        with open(argv[3], 'r') as file:
            text = file.read()

        result = encrypt(argv[2], text)

        if len(argv) == 3:
            with open(argv[4], 'w') as file:
                file.write(result)
        else:
            print(result)


if __name__ == '__main__':
    main()