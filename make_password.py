
import re

def add_to_words(listname, words):
    data = open(listname,"r").readlines()

    import string
    data = map(string.strip,data)

    P = re.compile("(\d+)\s+(\w+)")

    # parse the whole file
    for i in range(len(data)):
        m = P.search(data[i])
        if m is not None:
            # if you found a result
            # there is other junk in the file
            res = m.group(2)

            # then make sure the word is big enough
            if len(res)>3:
                words.append(m.group(2))

words = []
add_to_words("beale.wordlist.asc",words)
add_to_words("diceware.wordlist.asc",words)

import random
for j in range(10):
    for i in range(4):
        print random.choice(words),
    print
