import json

POST_PATH = "posts.json"

def load_post():
    with open(POST_PATH, encoding='utf-8', mode='r') as file:
        posts = json.load(file)
        return posts

def uploads_posts(posts):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)