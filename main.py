from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "welcome to my api!!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}

# stopped 1:13:30
