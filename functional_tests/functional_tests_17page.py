from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("D:\Downloads\chromedriver_win32\chromedriver.exe")
        # self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다.
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do' 를 표시하고 있다
        self.assertIn('To_Do', self.browser.title)
        self.fail('Finish the test!')

        # 그녀는 바로 작업을 추가 하기로 한다.


if __name__ == '__main__':
    unittest.main(warnings='ignore')

