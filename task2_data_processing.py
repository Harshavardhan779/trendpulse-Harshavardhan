import pandas as pd
import os
import glob

# Search for any JSON file in the data folder
json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("No files found! Run Task 1.")
else:
    # This picks the latest file based on creation time
    latest_file = max(json_files, key=os.path.getctime)
    
    # Load and immediately rename columns for Task 2 requirements
    df = pd.read_json(latest_file)
    df = df.rename(columns={'id': 'post_id', 'descendants': 'num_comments'})
    
    print(f"Loaded {len(df)} stories from {latest_file}")
    
# 1. Remove Duplicates
df.drop_duplicates(subset=['post_id'], inplace=True)
print(f"After removing duplicates: {len(df)}")

# 2. Missing values
# Use 'how="any"' to drop a row if any of these three are missing
df.dropna(subset=['post_id', 'title', 'score'], inplace=True)
print(f"After removing nulls: {len(df)}")

# 3. Data types
# Ensuring these are integers for later analysis
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# 4. Low quality filter
df = df[df['score'] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Whitespace stripping
df['title'] = df['title'].str.strip()    
# 1. Create the 'category' column
# Since the API doesn't give us categories, we'll assign them based on keywords
def assign_category(title):
    t = title.lower()
    if any(w in t for w in ['ai', 'tech', 'software', 'python', 'linux', 'code']):
        return 'technology'
    elif any(w in t for w in ['science', 'space', 'nasa', 'physics', 'bio']):
        return 'science'
    elif any(w in t for w in ['news', 'world', 'politics', 'court']):
        return 'worldnews'
    elif any(w in t for w in ['startup', 'money', 'business', 'job']):
        return 'business'
    else:
        return 'general'

df['category'] = df['title'].apply(assign_category)

# 2. Save the final cleaned data
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

# 3. Final Confirmation Messages
print(f"Saved {len(df)} rows to {output_file}")
print("\nStories per category:")
print(df['category'].value_counts())