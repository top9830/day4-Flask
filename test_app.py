import os
import tempfile
import unittest

from app import create_app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False)
        self.db_file.close()
        self.app = create_app(
            {
                "TESTING": True,
                "DATABASE": self.db_file.name,
            }
        )
        self.client = self.app.test_client()

    def tearDown(self):
        if os.path.exists(self.db_file.name):
            os.unlink(self.db_file.name)

    def test_posts_list_page_returns_200(self):
        response = self.client.get("/posts")

        self.assertEqual(response.status_code, 200)

    def test_new_post_page_returns_200(self):
        response = self.client.get("/posts/new")

        self.assertEqual(response.status_code, 200)

    def test_create_post_redirects_to_detail(self):
        response = self.client.post(
            "/posts",
            data={"title": "First Post", "content": "Hello from test"},
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/posts/", response.headers["Location"])

    def test_detail_page_shows_created_post(self):
        create_response = self.client.post(
            "/posts",
            data={"title": "Detail Title", "content": "Detail Content"},
            follow_redirects=False,
        )

        detail_response = self.client.get(create_response.headers["Location"])

        self.assertEqual(detail_response.status_code, 200)
        body = detail_response.get_data(as_text=True)
        self.assertIn("Detail Title", body)
        self.assertIn("Detail Content", body)


if __name__ == "__main__":
    unittest.main()
