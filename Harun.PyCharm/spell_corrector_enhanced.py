# Harun Altay

from spell import *
import sys
import time


def process_a_file_enhanced():
    argument_vector = sys.argv
    if len(argument_vector) != 3:
        print("usage: python spell_corrector corpus.txt test_words_misspelled.txt")
        exit()

    file_misspelled = open(argument_vector[2]).readlines()

    start = time.perf_counter()

    guessed_string = ""

    for line in file_misspelled:
        misspelled_word = line.strip()
        guessed_word = correction_enhanced(misspelled_word)
        if guessed_word == misspelled_word:
            guessed_string += "\n"
            continue
        guessed_string += guessed_word + "\n"

    guessed_string = guessed_string[:-1]

    dt = time.perf_counter() - start

    # print(guessed_string)

    f = open("output_spell_corrector_enhanced.txt", "w")
    f.write(guessed_string)
    f.close()

    print("time elapsed:", dt)


if __name__ == '__main__':
    process_a_file_enhanced()
