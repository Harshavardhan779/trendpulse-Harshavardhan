import os
import requests
from datetime import datetime
import json

# checkpoint-1
Folder='data'
if not os.path.exists(Folder):
    os.makedirs(Folder)
    
# checkpoint-2
date_str=datetime.now().strftime("%Y%m%d")
file_path=os.path.join(Folder,f"trends_{date_str}.json")

# checkopint-3
top_stories_url='https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {"User-Agent": "TrendPulse/1.0"}
response=requests.get(top_stories_url,headers=headers)
all_top_ids=response.json()
target_ids=all_top_ids[:120]

# checkpoint-4
stories=[]
for id in target_ids:
    item_url='https://hacker-news.firebaseio.com/v0/item/{id}.json' 
    items=requests.get(item_url,headers=headers).json()
    
    for items in items.get("type")=="story":
        story_dict={
           "id":items.get("id"),
           "title":items.get("title"),
           "url": items.get("url"),
                "score": items.get("score", 0),
                "by": items.get("by"),
                "time": items.get("time"),
                "descendants": items.get("descendants", 0) 
        }
    stories.append(story_dict)
    if len(stories)>=100:
        break
with open (file_path,'w') as f:
    json.dump(stories,indent=4)  
    
print(f"Collected {len(stories)} and saved in path {file_path}")              