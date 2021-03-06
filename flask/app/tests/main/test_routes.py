import unittest

from app import create_app, db
from config import TestConfig
from app.models import User, Content


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

        db.session.add(Content(releases="unique_data_release",
                               podcasts="unique_data_podcast"))
        db.session.commit()
        response = self.testapp.get("/audio", follow_redirects=True)
        self.assertTrue(b"unique_data_release" in response.data)
        self.assertTrue(b"unique_data_podcast" in response.data)

    def test_video(self):
        response = self.testapp.get("/video", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::video()" in response.data)

        db.session.add(Content(videos=b"unique_data_video"))
        db.session.commit()
        response = self.testapp.get("/video", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"unique_data_video" in response.data)

    def test_contact(self):
        response = self.testapp.get("/contact", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::contact()" in response.data)

        db.session.add(Content(contact="unique_contact_data"))
        db.session.commit()
        response = self.testapp.get("/contact", follow_redirects=True)
        self.assertTrue(b"unique_contact_data" in response.data)

    def test_bio(self):
        response = self.testapp.get("/bio", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::bio()" in response.data)

        db.session.add(Content(bio="unique_data_bio"))
        db.session.commit()
        response = self.testapp.get("/bio", follow_redirects=True)
        self.assertTrue(b"unique_data_bio" in response.data)

    def test_impressum(self):
        response = self.testapp.get("/impressum", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"::impressum()" in response.data)

        db.session.add(Content(impressum="unique_data_impressum"))
        db.session.commit()
        response = self.testapp.get("/impressum", follow_redirects=True)
        self.assertTrue(b"unique_data_impressum" in response.data)

    def test_cms_update_content(self):
        content = Content(bio="unique_data")
        db.session.add(content)
        db.session.commit()
        response = self.testapp.get("/bio", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertTrue(b"unique_data" in response.data)


if __name__ == '__main__':
    unittest.main()
