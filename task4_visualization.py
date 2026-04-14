import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Task 1: Setup ---
# Load the analysed data from Task 3
df = pd.read_csv('data/trends_analysed.csv')

# Create 'outputs' folder if it doesn't exist
output_dir = 'outputs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Helper function to shorten titles for the charts
def shorten_title(title):
    return title[:50] + '...' if len(title) > 50 else title

# --- Task 2: Chart 1 - Top 10 Stories by Score ---
plt.figure(figsize=(10, 6))
# Get top 10 stories sorted by score
top_10 = df.nlargest(10, 'score').sort_values('score', ascending=True)
short_titles = [shorten_title(t) for t in top_10['title']]

plt.barh(short_titles, top_10['score'], color='skyblue')
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.title('Top 10 Stories by Score')
plt.tight_layout()
plt.savefig(f'{output_dir}/chart1_top_stories.png')
plt.show()

# --- Task 3: Chart 2 - Stories per Category ---
plt.figure(figsize=(8, 6))
category_counts = df['category'].value_counts()
# Use a different color for each bar using a colormap
colors = plt.cm.Paired(range(len(category_counts)))

category_counts.plot(kind='bar', color=colors)
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.title('Distribution of Stories per Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{output_dir}/chart2_categories.png')
plt.show()

# --- Task 4: Chart 3 - Score vs Comments ---
plt.figure(figsize=(8, 6))
# Filter data for popular vs non-popular to color them differently
popular = df[df['is_popular'] == True]
non_popular = df[df['is_popular'] == False]

plt.scatter(non_popular['score'], non_popular['num_comments'], color='gray', alpha=0.5, label='Non-Popular')
plt.scatter(popular['score'], popular['num_comments'], color='orange', alpha=0.8, label='Popular')

plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.title('Relationship: Score vs Comments')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(f'{output_dir}/chart3_scatter.png')
plt.show()

# --- Bonus: Dashboard ---
# Create a dashboard layout (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('TrendPulse Dashboard', fontsize=20, fontweight='bold')

# Subplot 1: Top 10
axs[0, 0].barh(short_titles, top_10['score'], color='skyblue')
axs[0, 0].set_title('Top 10 Stories')

# Subplot 2: Categories
category_counts.plot(kind='bar', color=colors, ax=axs[0, 1])
axs[0, 1].set_title('Stories per Category')

# Subplot 3: Scatter
axs[1, 0].scatter(non_popular['score'], non_popular['num_comments'], color='gray', alpha=0.5)
axs[1, 0].scatter(popular['score'], popular['num_comments'], color='orange', alpha=0.8)
axs[1, 0].set_title('Score vs Comments')

# Hide the empty 4th subplot
axs[1, 1].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(f'{output_dir}/dashboard.png')
plt.show()

print(f"Success! 4 PNG files have been generated in the '{output_dir}/' folder.")