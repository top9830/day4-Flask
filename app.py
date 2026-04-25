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

    @app.get("/posts/new")
    def posts_new():
        return render_template("posts_new.html")

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
        db = get_db()
        post = db.execute(
            "SELECT id, title, content, created_at FROM posts WHERE id = ?",
            (post_id,),
        ).fetchone()

        if post is None:
            abort(404)

        return render_template("posts_detail.html", post=post)

    with app.app_context():
        init_db()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
