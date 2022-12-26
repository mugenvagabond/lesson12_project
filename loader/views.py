from flask import Blueprint, render_template, request
from functions import save_picture, add_post
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post")
def create_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=['POST'])
def create_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Данные не загружены'

    picture_path = save_picture(picture)
    if not picture_path:
        logging.info(f'Файл {picture.filename} не изображение!')
        return 'Неверный формат'
    post = {'pic': picture_path, 'content': content}

    post = add_post(post)

    return render_template('post_uploaded.html', post=post)

