
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Close the browser now:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # TODO: There is still a text box inviting heer to add another item
        # TODO: You enter 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # TODO: The page updates again and now shows both entries.
        table = self.browser.find_element_by_id('id_list_table')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # TODO: Will the site remember the list?  The site should have generated a
        # TODO: unique URL ... explanatory text to that effect

        # TODO: You visit the URL - the to-do list is still there

        # TODO: All is OK
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')







