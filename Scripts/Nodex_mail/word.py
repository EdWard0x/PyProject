import random

from random_word import RandomWords

def getrandomwords():
    r = RandomWords()
    with open('words.txt', 'w') as fw:
        for i in range(50):
            arr = r.get_random_words()
            for j in arr:
                fw.write(str(j) + ',')

# getrandomwords()

def get_words():

    with open('words.txt', 'r') as fr:
        B = fr.read()

    A = B.split(',')
    for i in range(len(A)):
        print(A[i])
    # print(type(A))
    # print(A)

# get_words()
with open('words.txt', 'r') as fr:
    words = fr.read().split(',')
words_index1 = random.randint(0, len(words))
words_index2 = random.randint(0, len(words))
# print(words[words_index1])
random_m = str(words[words_index1]) + str(words[words_index2]) + str(random.randint(0, 9)) + str(random.randint(0, 50))
print(random_m)
print(len(words))

