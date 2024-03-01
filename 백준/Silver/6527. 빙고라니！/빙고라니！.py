from math import gcd
import re
words_count = 0
bs_count = 0
unique_words = set()

try:
    while True:
        line = input()
        line = re.sub(r'[^a-zA-Z]', ' ', line).upper()
        words = line.split()
        
        for word in words:
            if word == "BULLSHIT":
                bs_count += 1
                words_count += len(unique_words)
                unique_words.clear()
            else:
                unique_words.add(word)
except EOFError:
    pass 

if words_count == 0 or bs_count == 0:
    print("0 / 0")
else:
    divisor = gcd(words_count, bs_count)
    print(f"{words_count // divisor} / {bs_count // divisor}")
