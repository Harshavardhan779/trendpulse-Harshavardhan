import pandas as pd
import numpy as np
import os

# --- Task 1: Load and Explore ---
# Defining the file path from Task 2
input_file = 'data/trends_clean.csv'

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found. Please run Task 2 first.")
else:
    # Load the cleaned dataset
    df = pd.read_csv(input_file)
    
    # Print the shape and first 5 rows
    print(f"Loaded data: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Basic averages using Pandas
    avg_score = df['score'].mean()
    avg_comments = df['num_comments'].mean()
    
    print(f"\nAverage score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}")

    # --- Task 2: Basic Analysis with NumPy ---
    print("\n--- NumPy Stats ---")
    
    # Converting columns to NumPy arrays for specific statistical analysis
    scores_array = df['score'].to_numpy()
    comments_array = df['num_comments'].to_numpy()

    # Calculating statistics using NumPy functions
    mean_score = np.mean(scores_array)
    median_score = np.median(scores_array)
    std_score = np.std(scores_array)
    max_score = np.max(scores_array)
    min_score = np.min(scores_array)

    print(f"Mean score   : {mean_score:.2f}")
    print(f"Median score : {median_score:.2f}")
    print(f"Std deviation: {std_score:.2f}")
    print(f"Max score    : {max_score}")
    print(f"Min score    : {min_score}")

    # Finding which category has the most stories
    # We use value_counts() and idxmax() to find the top label
    mode_category = df['category'].value_counts().idxmax()
    category_count = df['category'].value_counts().max()
    print(f"Most stories in: {mode_category} ({category_count} stories)")

    # Finding the story with the most comments
    max_comm_idx = np.argmax(comments_array)
    most_commented_title = df.iloc[max_comm_idx]['title']
    most_commented_count = df.iloc[max_comm_idx]['num_comments']
    print(f"Most commented story: \"{most_commented_title}\" — {most_commented_count} comments")

    # --- Task 3: Add New Columns ---
    # Formula: engagement = num_comments / (score + 1)
    # Adding 1 prevents a division by zero error if a score is 0
    df['engagement'] = df['num_comments'] / (df['score'] + 1)

    # is_popular: True if score is strictly greater than the average score
    df['is_popular'] = df['score'] > avg_score
    
    # Optional: Print first 5 rows again to show new columns
    print("\nUpdated DataFrame with Engagement and Popularity:")
    print(df[['title', 'engagement', 'is_popular']].head())

    # --- Task 4: Save the Result ---
    output_file = 'data/trends_analysed.csv'
    df.to_csv(output_file, index=False)
    print(f"\nSaved to {output_file}")