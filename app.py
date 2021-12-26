from flask import Flask, request, render_template, send_from_directory, abort
from functions import read_post, get_tags, get_posts_by_tag

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', tags=get_tags(read_post(POST_PATH)))


@app.route("/tag/")
def page_tag():
    tag = request.args.get('tag')
    if not tag:
        abort(400)
    data = read_post(POST_PATH)
    posts = get_posts_by_tag(data, tag)
    return render_template('post_by_tag.html', tag=tag, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True)

