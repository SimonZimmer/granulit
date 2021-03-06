import unittest
from app import create_app, db
from config import TestConfig
from app.models import User, Content, load_user


class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.testapp = self.app.test_client()

        user = User(username="test_user")
        user.set_password("test_password")
        db.session.add(user)
        db.session.commit()

    def test_check_password(self):
        with self.app.app_context():
            user = User.query.filter_by(username="test_user").first()
            self.assertTrue(user.check_password("test_password"))

    def test_set_password(self):
        with self.app.app_context():
            user = User.query.filter_by(username="test_user").first()
            user.set_password("new_password")
            self.assertTrue(user.check_password("new_password"))


class TestContent(unittest.TestCase):
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

    def test_latest(self):
        content_old = Content(bio="a", releases="b", podcasts="c",
                              videos="d", contact="e", impressum="f")
        content_new = Content(bio="aa", releases="bb", podcasts="cc",
                              videos="dd", contact="ee", impressum="ff")
        db.session.add(content_old)
        db.session.add(content_new)
        db.session.commit()

        latest = Content().latest()
        self.assertEqual("aa", latest.bio)
        self.assertEqual("bb", latest.releases)
        self.assertEqual("cc", latest.podcasts)
        self.assertEqual("dd", latest.videos)
        self.assertEqual("ee", latest.contact)
        self.assertEqual("ff", latest.impressum)

    def test_dict_conversion(self):
        content = Content(bio="aaa", releases="bbb", podcasts="ccc",
                          videos="ddd", contact="eee", impressum="fff")

        try:
            content_dict = dict(content)['content']
            self.assertEqual("aaa", content_dict['bio'])
            self.assertEqual("bbb", content_dict['releases'])
            self.assertEqual("ccc", content_dict['podcasts'])
            self.assertEqual("ddd", content_dict['videos'])
            self.assertEqual("eee", content_dict['contact'])
            self.assertEqual("fff", content_dict['impressum'])
        except:
            self.fail("dict conversion failed")


if __name__ == '__main__':
    unittest.main()