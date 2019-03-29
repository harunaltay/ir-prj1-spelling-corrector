import sys


def compare_two_file():
    argument_vector = sys.argv
    if len(argument_vector) != 3:
        print("usage: python accuracy_corrector file_guessed.txt file_correct.txt")
        exit()

    list_guessed = open(argument_vector[1]).readlines()
    list_correct = open(argument_vector[2]).readlines()

    len_list_guessed = len(list_guessed)
    len_list_correct = len(list_correct)

    if len_list_guessed != len_list_correct:
        print("Either some first or some last element of guessed list is empty.")
        print("So, this program will not work correctly in such a case. Sorry. Halting.")
        exit()

    number_of_empty_guess = 0
    number_of_wrong_guess = 0

    for i in range(len_list_correct):
        word_guessed = list_guessed[i].strip()
        word_correct = list_correct[i].strip()

        if word_guessed == "":
            number_of_empty_guess += 1
            print(word_guessed, "-", word_correct)
            continue

        if word_guessed != word_correct:
            number_of_wrong_guess += 1
            print(word_guessed, "-", word_correct)

    print("number_of_empty_guess:", number_of_empty_guess)
    print("number_of_wrong_guess:", number_of_wrong_guess)

    total_not_correctly_guessed = number_of_empty_guess + number_of_wrong_guess
    print("total_not_correctly_guessed:", total_not_correctly_guessed)

    correct_guessed = 384 - total_not_correctly_guessed
    print("correct_guessed:", correct_guessed)

    correct_percent = correct_guessed / 384
    print("correct_percent:", correct_percent)


if __name__ == '__main__':
    compare_two_file()
