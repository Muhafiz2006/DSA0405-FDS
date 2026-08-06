import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('./students_performance.csv')

# Convert the three exam scores into an overall percentage, then bucket
# into a letter grade using standard cutoffs
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

def to_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

df['Grade'] = df['average_score'].apply(to_grade)

freq = df['Grade'].value_counts().sort_index()
print("Frequency distribution of grades (derived from average of math/reading/writing scores):")
print(freq)

plt.figure(figsize=(7,5))
order = ['A','B','C','D','F']
vals = [freq.get(g, 0) for g in order]
bars = plt.bar(order, vals, color=['#4C72B0','#55A868','#C44E52','#8172B2','#CCB974'])
plt.title('Frequency Distribution of Student Grades', fontsize=13, fontweight='bold')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
for b in bars:
    plt.text(b.get_x()+b.get_width()/2, b.get_height()+2, str(int(b.get_height())), ha='center')
plt.tight_layout()
plt.savefig('./task2_grade_bar.png', dpi=150)
print("\nChart saved.")
