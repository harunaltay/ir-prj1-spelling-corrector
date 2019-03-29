from spell import *
import sys


argument_vector = sys.argv

print(argument_vector)
print(type(argument_vector))
print(len(argument_vector))

if len(argument_vector) != 2:
    print("usage: python spell_corrector input_file.txt")
    exit()

file_name = argument_vector[1]

print(file_name)

