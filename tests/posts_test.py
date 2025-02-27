import pytest

# Тест создания поста
def test_create_post(session, base_url):
    url = f"{base_url}/posts"
    data = {"title": "test", "body": "content", "userId": 1}
    response = session.post(url, json=data)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = response.json()
    assert json_data["title"] == data["title"]
    assert json_data["body"] == data["body"]
    assert json_data["userId"] == data["userId"]

# Тест получения списка постов
def test_get_posts(session, base_url):
    url = f"{base_url}/posts"
    response = session.get(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert isinstance(response.json(), list)

# Тест получения поста по id
@pytest.mark.parametrize("post_id", [1, 15, 50])
def test_get_post_by_id(session, base_url, post_id):
    url = f"{base_url}/posts/{post_id}"
    response = session.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == post_id

# Тест обновления поста PUT
def test_update_post_put(session, base_url):
    post_id = 1
    url = f"{base_url}/posts/{post_id}"
    data = {"id": post_id, "title": "updated", "body": "my updated content :)", "userId": 1}
    response = session.put(url, json=data)

    assert response.status_code == 200
    assert response.json()["title"] == data["title"]

# Тест частичного обновления поста PATCH
def test_update_post_patch(session, base_url):
    post_id = 1
    url = f"{base_url}/posts/{post_id}"
    data = {"title": "patched"}
    response = session.patch(url, json=data)

    assert response.status_code == 200
    assert response.json()["title"] == data["title"]

# Тест удаления поста
def test_delete_post(session, base_url):
    post_id = 1
    url = f"{base_url}/posts/{post_id}"
    response = session.delete(url)

    assert response.status_code == 200
    assert response.json() == {}

# Тест запроса несуществующего поста
def test_get_none_post(session, base_url):
    url = f"{base_url}/posts/9999"
    response = session.get(url)

    assert response.status_code == 404 or response.json() == {}
