from flask import Blueprint, render_template, request
import logging
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def main_page():
    return render_template('index.html')


@main_blueprint.route("/search")
def search_page():
    substr = request.args.get('s')
    logging.info(f'Выполняется поиск по слову: {substr}')
    posts = get_posts_by_word(substr)
    return render_template('post_list.html', substr=substr, posts=posts)

