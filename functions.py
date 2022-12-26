import json
import logging


def load_posts() -> list[dict]:
    """Загрузка json"""
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f'Ошибка при загрузке файла: {e}')
        return []


def get_posts_by_word(word: str) -> list[dict]:
    """Поиск поста по слову"""
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    """Сохранение изображения"""
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['jpg', 'png', 'jpeg']:
        return

    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'


def add_post(post: dict) -> dict:
    """Добавление поста"""
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post

