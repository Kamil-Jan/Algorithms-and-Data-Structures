import re, math, time
from collections import Counter
from functools import reduce


D1 = "C:\\Users\\Администратор\\Desktop\\1.txt"
D2 = "C:\\Users\\Администратор\\Desktop\\2.txt"


def get_vector_length(doc):
    with open(doc, 'r') as file:
        doc_words = re.findall(r'\w+', file.read())
        words_freq = Counter(doc_words)

    length = 0
    for word in dict(words_freq):
        length += words_freq[word] ** 2
    return (words_freq, length)

freq1, doc1_length = get_vector_length(D1)
freq2, doc2_length = get_vector_length(D2)

same_w = dict(freq1 & freq2)
D1D2 = reduce(int.__add__, [freq1[word]*freq2[word] for word in same_w])

distance = math.acos(D1D2 / math.sqrt(doc1_length * doc2_length))
print(distance)

