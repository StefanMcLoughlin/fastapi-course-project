from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    posts_list = [schemas.PostOut(**post) for post in res.json()]
    
    assert res.status_code == 200
    assert len(posts_list) == len(test_posts)

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_found(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title
    assert res.status_code == 200


@pytest.mark.parametrize("title, content, published", [
    ("awesome new title", "awesome new content", True),
    ("favorit pizza", "i love magaritha", False),
    ("tallest skyscraper", "wahoo", True),
])
def test_create_post(authorized_client, test_user, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]

def test_create_post_default_published_true(authorized_client, test_user):
    res = authorized_client.post("/posts/", json={"title": "arbitrary title", "content": "bla bla bla"})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "arbitrary title"
    assert created_post.content == "bla bla bla"
    assert created_post.published is True
    assert created_post.owner_id == test_user["id"]

def test_unauthorized_user_create_post(client):
    res = client.post("/posts/", json={"title": "arbitrary title", "content": "bla bla bla"})
    assert res.status_code == 401