#the most repetitive character in a sentence
from pprint import pprint
sentence = "the quick brown fox jumps over the lazy dog"

char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

char_freq_sorted=sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

print(char_freq_sorted[0])
