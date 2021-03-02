import unittest

from app import create_app
from config import TestConfig


def login(testapp, username, password, redirect=False):
    return testapp.post('/login', data=dict(
            username=username,
            password=password,
            remember_me=False,
        ), follow_redirects=redirect)


def logout(testapp, redirect = False):
    return testapp.get('/logout', follow_redirects=redirect)


class AuthRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        @self.app.context_processor
        def utility_processor():
            def app_version():
                return self.app.config["VERSION"]

            return dict(app_version=app_version)
        self.testapp = self.app.test_client()

    def test_login_logout(self):
        response = login(self.testapp, "testing", "testing")
        self.assertTrue("/cms" in response.headers['location'])
        self.assertEqual(302, response.status_code)

        response = logout(self.testapp)
        self.assertTrue("/login" in response.headers['location'])
        self.assertEqual(302, response.status_code)

   # def test_login_failure(self):
   #     response = login(self.testapp, "wrong_user", "wrong_pass")
   #     self.assertTrue("/login" in response.headers['location'])
   #     self.assertEqual(302, response.status_code)
#
 #   def test_login_get(self):
 #       response = self.testapp.get("/login", follow_redirects=True);
  #      self.assertTrue(b"<h1>Login</h1>" in response.data)
   #     self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()