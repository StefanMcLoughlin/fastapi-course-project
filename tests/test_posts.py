from app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    posts_list = [schemas.PostOut(**post) for post in res.json()]
    
    assert res.status_code == 200
    assert len(posts_list) == len(test_posts)

