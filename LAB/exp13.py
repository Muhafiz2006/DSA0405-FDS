import string
from collections import Counter

# Read the text document
with open("sample_text.txt", "r") as file:
    text = file.read()

# Preprocess: lowercase and remove punctuation
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words and count frequency
words = text.split()
word_freq = Counter(words)

# Display the frequency distribution (most common first)
print("Word Frequency Distribution:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
