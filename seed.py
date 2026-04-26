import sqlite3
from crawler import fetch_rss, parse_items, RSS_URL

DB_PATH = "board.db"


def seed():
    print("구글 뉴스 한국어 RSS를 가져오는 중...\n")
    soup = fetch_rss(RSS_URL)
    items = parse_items(soup)

    conn = sqlite3.connect(DB_PATH)
    db = conn.cursor()
    db.execute(
        """CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )"""
    )

    added = 0
    for it in items:
        exists = db.execute("SELECT 1 FROM posts WHERE title = ?", (it["title"],)).fetchone()
        if exists:
            continue
        db.execute(
            "INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)",
            (it["title"], f"{it['summary']}\n\n{it['link']}", it["pub_date"]),
        )
        added += 1

    conn.commit()
    conn.close()
    print(f"{added}건 추가됨 (중복 제외: {len(items) - added}건)")


if __name__ == "__main__":
    seed()
