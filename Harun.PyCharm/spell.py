"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html
Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

################ Spelling Corrector 

import re
from collections import Counter


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('corpus.txt').read()))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def correction_enhanced(word):
    "Most probable spelling correction for word."
    return max(candidates_enhanced(word), key=P)


def candidates(word): 
    "Generate possible spelling corrections for word."
    # return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    return (known([word]) or known(edits1(word)) or [word])


def candidates_enhanced(word):
    "Generate possible spelling corrections for word."
    # return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    return (known([word]) or known(edits1_enhanced(word)) or [word])


def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits1_enhanced(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]

    total = deletes + transposes + replaces + inserts
    # print("type(total) :", type(total)) -> list

    total_list_enhanced = []

    start_letter = word[0]

    for line in total:
        if line[0] != start_letter:
            continue
        total_list_enhanced.append(line)

    return set(total_list_enhanced)


if __name__ == '__main__':
    print("merhaba")


# use instead of time.clock() deprecated :
# time.perf_counter()
# or
# time.process_time()
