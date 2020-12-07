from nltk.corpus import *

word_list = words.words()


def store():
    run = word_list
    data = []
    for i in run:
        if len(i) <= 5:
            data.append(i)

    return data


if __name__ == '__main__':
    a = store()
    print(a)
