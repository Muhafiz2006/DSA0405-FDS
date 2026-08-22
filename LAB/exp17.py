import string
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Common stop words that don't carry significant meaning
STOP_WORDS = {
    "the", "a", "an", "and", "is", "it", "of", "to", "in", "on", "for",
    "was", "were", "with", "this", "that", "i", "my", "but", "at", "as",
    "are", "be", "so", "very", "has", "have", "had", "not", "will",
    "would", "could", "can", "just", "if", "or", "we", "you", "your"
}


def load_feedback(csv_path):
    """Load the dataset from a CSV file containing a 'feedback' column."""
    df = pd.read_csv(csv_path)
    return df["feedback"].astype(str).tolist()


def preprocess(text):
    """Lowercase, strip punctuation, and remove stop words."""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return [w for w in words if w not in STOP_WORDS]


def compute_word_frequency(feedback_list):
    """Calculate the frequency distribution of words across all feedback entries."""
    freq = Counter()
    for entry in feedback_list:
        freq.update(preprocess(entry))
    return freq


def plot_top_n(freq, n):
    """Plot a bar graph of the top N most frequent words."""
    top_words = freq.most_common(n)
    words, counts = zip(*top_words)

    plt.figure(figsize=(8, 5))
    plt.bar(words, counts, color="darkorange")
    plt.title(f"Top {n} Most Frequent Words in Customer Feedback")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    feedback_list = load_feedback("data.csv")
    word_freq = compute_word_frequency(feedback_list)

    n = int(input("Enter the number of top words to display: "))

    print(f"\nTop {n} Most Frequent Words:")
    for word, count in word_freq.most_common(n):
        print(f"{word}: {count}")

    plot_top_n(word_freq, n)
