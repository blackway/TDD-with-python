
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # Close the browser now:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Get the home page of our application:
        self.browser.get('http://localhost:8000')

        # Check for our initial code change - check To-Do appears in the title:
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # TODO: You are invited to do a todo item straight away

        # TODO: You type 'Buy peacock feathers' into a text box

        # TODO: When you hit enter, the page updates, and page now lists
        # TODO: '1: Buy peacock feathers' as an item in the to-do list

        # TODO: There is still a text box inviting heer to add another item
        # TODO: You enter 'Use peacock feathers to make a fly'

        # TODO: The page updates again and now shows both entries.

        # TODO: Will the site remember the list?  The site should have generated a
        # TODO: unique URL ... explanatory text to that effect

        # TODO: You visit the URL - the to-do list is still there

        # TODO: All is OK


if __name__ == '__main__':
    unittest.main(warnings='ignore')







