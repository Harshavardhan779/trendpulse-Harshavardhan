import os
import requests
from datetime import datetime
import json

# checkpoint-1
Folder = 'data'
if not os.path.exists(Folder):
    os.makedirs(Folder)

# checkpoint-2
date_str = datetime.now().strftime("%Y%m%d")
file_path = os.path.join(Folder, f"trends_{date_str}.json")

# checkpoint-3
top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {"User-Agent": "TrendPulse/1.0"}

response = requests.get(top_stories_url, headers=headers)
all_top_ids = response.json()
target_ids = all_top_ids[:120]

# checkpoint-4
stories = []

for id in target_ids:
    item_url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    item = requests.get(item_url, headers=headers).json()

    # skip if not story or invalid
    if not item or item.get("type") != "story":
        continue

    story_dict = {
        "id": item.get("id"),
        "title": item.get("title"),
        "url": item.get("url"),
        "score": item.get("score", 0),
        "by": item.get("by"),
        "time": item.get("time"),
        "descendants": item.get("descendants", 0)
    }

    stories.append(story_dict)

    if len(stories) >= 100:
        break

# save file
with open(file_path, 'w') as f:
    json.dump(stories, f, indent=4)

print(f"Collected {len(stories)} stories and saved at {file_path}.")