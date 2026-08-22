import pandas as pd

# User interaction data: number of likes received by each post
data = {
    'PostID': list(range(1, 13)),
    'Likes': [120, 85, 120, 200, 85, 45, 120, 200, 85, 60, 45, 120]
}
df = pd.DataFrame(data)

# Frequency distribution of likes among the posts
likes_freq = df['Likes'].value_counts().sort_index()

print("Frequency Distribution of Likes Among Posts:")
print(likes_freq)
