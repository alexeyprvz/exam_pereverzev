import app
import unittest as ut

class TestMyApp(ut.TestCase):

    def SetUp(self):
        self.app = app

    def test_now_time(self):
        self.assertTrue(app.factorial(5) == 120)

    def tearDown(self):
        pass

if __name__ == '__main__':
    ut.main()