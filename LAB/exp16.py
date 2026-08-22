import string
from collections import Counter

# Customer reviews dataset for a product
reviews = [
    "The product quality is amazing and delivery was fast",
    "Delivery was late but the product quality is great",
    "Great value for money, I love this product",
    "The product broke after a week, poor quality",
    "Fast delivery and amazing customer service",
    "I love the design but the quality could be better",
    "Amazing product, will definitely buy again",
    "Poor packaging led to a damaged product on delivery",
    "Great customer service and fast delivery every time",
    "The price is high for the quality offered"
]

# Preprocess: lowercase and remove punctuation
word_freq = Counter()
for review in reviews:
    review = review.lower().translate(str.maketrans('', '', string.punctuation))
    words = review.split()
    word_freq.update(words)

# Display the frequency distribution (most common first)
print("Word Frequency Distribution in Customer Reviews:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
