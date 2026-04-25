import sqlite3
from pathlib import Path

from flask import Flask, abort, g, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=str(BASE_DIR / "board.db"),
    )

    if test_config:
        app.config.update(test_config)

    def get_db():
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
        return g.db

    def init_db():
        db = get_db()
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        db.commit()

    @app.teardown_appcontext
    def close_db(_error):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    @app.get("/")
    def root():
        return redirect(url_for("posts_list"))

    @app.get("/posts")
    def posts_list():
        db = get_db()
        posts = db.execute(
            "SELECT id, title, content, created_at FROM posts ORDER BY id DESC"
        ).fetchall()
        return render_template("posts_list.html", posts=posts)

    def get_post_or_404(post_id):
        db = get_db()
        post = db.execute(
            "SELECT id, title, content, created_at FROM posts WHERE id = ?",
            (post_id,),
        ).fetchone()
        if post is None:
            abort(404)
        return post

    @app.get("/posts/new")
    def posts_new():
        return render_template(
            "posts_new.html",
            page_title="The Journal - New Entry",
            submit_label="Publish",
            form_action=url_for("posts_create"),
            back_url=url_for("posts_list"),
            post=None,
        )

    @app.post("/posts")
    def posts_create():
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        db = get_db()
        cursor = db.execute(
            "INSERT INTO posts (title, content, created_at) VALUES (?, ?, CURRENT_TIMESTAMP)",
            (title, content),
        )
        db.commit()

        return redirect(url_for("posts_detail", post_id=cursor.lastrowid))

    @app.get("/posts/<int:post_id>")
    def posts_detail(post_id):
        post = get_post_or_404(post_id)
        return render_template("posts_detail.html", post=post)

    @app.get("/posts/<int:post_id>/edit")
    def posts_edit(post_id):
        post = get_post_or_404(post_id)
        return render_template(
            "write.html",
            page_title="The Journal - Edit Entry",
            submit_label="Update",
            form_action=url_for("posts_update", post_id=post_id),
            back_url=url_for("posts_detail", post_id=post_id),
            post=post,
        )

    @app.post("/posts/<int:post_id>/edit")
    def posts_update(post_id):
        get_post_or_404(post_id)
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        db = get_db()
        db.execute(
            "UPDATE posts SET title = ?, content = ? WHERE id = ?",
            (title, content, post_id),
        )
        db.commit()
        return redirect(url_for("posts_detail", post_id=post_id))

    @app.post("/posts/<int:post_id>/delete")
    def posts_delete(post_id):
        get_post_or_404(post_id)
        db = get_db()
        db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        db.commit()
        return redirect(url_for("posts_list"))

    with app.app_context():
        init_db()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
