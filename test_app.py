import os
import tempfile
import unittest

from app import create_app


class AppTestCase(unittest.TestCase):
    def _create_post(self, title="Title", content="Content"):
        response = self.client.post(
            "/posts",
            data={"title": title, "content": content},
            follow_redirects=False,
        )
        post_id = int(response.headers["Location"].rstrip("/").split("/")[-1])
        return post_id

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
        post_id = self._create_post("Detail Title", "Detail Content")

        detail_response = self.client.get(f"/posts/{post_id}")

        self.assertEqual(detail_response.status_code, 200)
        body = detail_response.get_data(as_text=True)
        self.assertIn("Detail Title", body)
        self.assertIn("Detail Content", body)

    def test_edit_page_returns_200_and_prefills_content(self):
        post_id = self._create_post("Edit Title", "Edit Content")

        response = self.client.get(f"/posts/{post_id}/edit")

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("Edit Title", body)
        self.assertIn("Edit Content", body)

    def test_update_post_redirects_to_detail_with_updated_content(self):
        post_id = self._create_post("Before", "Old Content")

        update_response = self.client.post(
            f"/posts/{post_id}/edit",
            data={"title": "After", "content": "New Content"},
            follow_redirects=False,
        )

        self.assertEqual(update_response.status_code, 302)
        self.assertEqual(update_response.headers["Location"], f"/posts/{post_id}")

        detail_response = self.client.get(f"/posts/{post_id}")
        body = detail_response.get_data(as_text=True)
        self.assertIn("After", body)
        self.assertIn("New Content", body)
        self.assertNotIn("Before", body)

    def test_delete_post_removes_post_and_redirects_to_list(self):
        post_id = self._create_post("Delete Me", "To Be Removed")

        delete_response = self.client.post(f"/posts/{post_id}/delete", follow_redirects=False)

        self.assertEqual(delete_response.status_code, 302)
        self.assertEqual(delete_response.headers["Location"], "/posts")

        detail_response = self.client.get(f"/posts/{post_id}")
        self.assertEqual(detail_response.status_code, 404)

    def test_detail_page_has_edit_delete_and_delete_confirm_prompt(self):
        post_id = self._create_post("Button Title", "Button Content")

        response = self.client.get(f"/posts/{post_id}")

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn(f"/posts/{post_id}/edit", body)
        self.assertIn(f"/posts/{post_id}/delete", body)
        self.assertIn("정말 삭제할까요?", body)


if __name__ == "__main__":
    unittest.main()
