from flask import Blueprint, request, render_template
from functions import load_post, uploads_posts

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')

@loader_blueprint.route('/', )
def loader():
    return render_template('post_form.html')

@loader_blueprint.route('/upload/', methods=['POST'])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        file.save(f"./uploads/{filename}")
        content = request.values['content']
        posts = load_post()
        posts.append({
            'pic': f'/uploads/{filename}',
            'content': content
        })
        uploads_posts(posts)
    except FileNotFoundError:
        return "<h1>Файл не найден</h1>"
    else:
        return render_template('post_uploaded.html', file=file, content=content)


