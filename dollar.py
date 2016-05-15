import urllib.request
import argparse

letter_values = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    '\n': 0,
    '\'': 0,
    'â': 1,
    'á': 1,
    'ä': 1,
    'ç': 3,
    'é': 5,
    'è': 5,
    'í': 8,
    'ó': 15,
    'ö': 15,
    'ô': 15,
    'ú': 21,
    'ü': 21,
    'û': 21,
    'ñ': 14
}

def get_value(letter):
    return letter_values[letter]

parser = argparse.ArgumentParser(description="Finds all the $1.00 words in a list.")
group = parser.add_mutually_exclusive_group()

group.add_argument('--input', dest='input', required=False)
group.add_argument('--output', dest='output', required=False)
group.add_argument('--value', dest='value', required=False)

args = parser.parse_args()

source = 'https://raw.githubusercontent.com/medude/one-dollar-word/master/unix_words'
target_score = 100

if args.input:
    source = args.input

if args.value:
    target_score = args.value

all_words = urllib.request.urlopen(source).read()

try:
    all_words = str(all_words, 'utf-8')
except:
    all_words = str(all_words, 'ascii')
    
all_words = all_words.lower().split()

for word in all_words[:]:
    score = 0
    for letter in word:
        score += get_value(letter)
    if score != target_score:
        all_words.remove(word)

if args.output:
    file = open(args.output, 'w')
    for word in all_words:
        file.write(word+'\n')
else:
    for word in all_words:
        print(word)
