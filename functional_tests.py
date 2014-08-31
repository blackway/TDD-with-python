
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Close the browser now:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Get the home page of our application:
        self.browser.get('http://localhost:8000')

        # Page title and header contain 'To-Do' lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # TODO: You are invited to do a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # TODO: You type 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # TODO: When you hit enter, the page updates, and page now lists
        # TODO: '1: Buy peacock feathers' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.browser.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # TODO: There is still a text box inviting heer to add another item
        # TODO: You enter 'Use peacock feathers to make a fly'
        #inputbox.send_keys('Use peacock feathers to make a fly')

        # TODO: The page updates again and now shows both entries.

        # TODO: Will the site remember the list?  The site should have generated a
        # TODO: unique URL ... explanatory text to that effect

        # TODO: You visit the URL - the to-do list is still there

        # TODO: All is OK
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')







