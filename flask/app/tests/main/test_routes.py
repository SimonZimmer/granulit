import unittest

from app import create_app, db
from config import TestConfig


class MainRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.testapp = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.testapp.get("/", follow_redirects=True)
        self.assertTrue(b"initializing..." in response.data)
        self.assertEqual(200, response.status_code)

        response = self.testapp.get("/index", follow_redirects=True)
        self.assertTrue(b"initializing..." in response.data)
        self.assertEqual(200, response.status_code)

    def test_audio(self):
        response = self.testapp.get("/audio", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::audio()" in response.data)

    def test_video(self):
        response = self.testapp.get("/video", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::video()" in response.data)

    def test_contact(self):
        response = self.testapp.get("/contact", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::contact()" in response.data)

    def test_bio(self):
        response = self.testapp.get("/bio", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::bio()" in response.data)

    def test_impressum(self):
        response = self.testapp.get("/impressum", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::impressum()" in response.data)

    def test_cms(self):
        response = self.testapp.get("/cms", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"<h1>Content Management System</h1>" in response.data)


if __name__ == '__main__':
    unittest.main()
