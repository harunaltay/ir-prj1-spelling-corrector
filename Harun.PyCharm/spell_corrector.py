from spell import *
import sys
import time

start = time.perf_counter()

argument_vector = sys.argv

print(argument_vector)
print(type(argument_vector))
print(len(argument_vector))

if len(argument_vector) != 3:
    print("usage: python spell_corrector corpus.txt test_words_misspelled.txt")
    exit()

# file_corpus = open(argument_vector[1])
file_misspelled = open(argument_vector[2]).readlines()

# print(file_corpus)
print(file_misspelled)

good, unknown = 0, 0
guessed_list = []

for line in file_misspelled:
    # print(line, end="")
    misspelled_word = line.strip()
    guessed_word = correction(misspelled_word)
    if guessed_word == misspelled_word:
        guessed_list.append("\n")
        print("------- could not geussed:", misspelled_word)
        continue
    guessed_list.append(guessed_word)
    print(guessed_word, "-", misspelled_word)
    # break


dt = time.perf_counter() - start

print("time elapsed:", dt)
