import re
import sys
import io
import csv
import json
import argparse
import requests
from bs4 import BeautifulSoup
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

RSS_URL = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"


def fetch_rss(url: str) -> BeautifulSoup:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, "xml")


def parse_items(soup: BeautifulSoup) -> list[dict]:
    items = []
    for item in soup.find_all("item")[:10]:
        pub_date = item.pubDate.text.strip() if item.pubDate else ""
        try:
            dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S GMT")
            pub_date = dt.strftime("%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            pass

        items.append({
            "title": item.title.text.strip() if item.title else "",
            "link": item.link.text.strip() if item.link else "",
            "summary": re.sub(r"<[^>]+>", "", item.description.text.strip()) if item.description else "",
            "pub_date": pub_date,
        })
    return items


def print_items(items: list[dict]):
    for i, it in enumerate(items, 1):
        print(f"[{i}] {it['title']}")
        print(f"    시간: {it['pub_date']}")
        print(f"    링크: {it['link']}")
        if it["summary"]:
            summary = it["summary"][:100] + ("..." if len(it["summary"]) > 100 else "")
            print(f"    요약: {summary}")
        print()


def save_json(items: list[dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"JSON 저장 완료: {path}")


def save_csv(items: list[dict], path: str):
    fields = ["title", "pub_date", "link", "summary"]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(items)
    print(f"CSV 저장 완료: {path}")


def main():
    parser = argparse.ArgumentParser(description="뉴스 RSS 크롤러")
    parser.add_argument("--output", "-o", choices=["console", "json", "csv", "all"], default="all",
                        help="출력 형식 (기본값: all)")
    parser.add_argument("--json-file", default="news.json", help="JSON 저장 파일명")
    parser.add_argument("--csv-file", default="news.csv", help="CSV 저장 파일명")
    args = parser.parse_args()

    print("구글 뉴스 한국어 RSS를 가져오는 중...\n")
    soup = fetch_rss(RSS_URL)
    items = parse_items(soup)

    if args.output in ("console", "all"):
        print(f"=== 최신 뉴스 {len(items)}건 ===\n")
        print_items(items)

    if args.output in ("json", "all"):
        save_json(items, args.json_file)

    if args.output in ("csv", "all"):
        save_csv(items, args.csv_file)


if __name__ == "__main__":
    main()
