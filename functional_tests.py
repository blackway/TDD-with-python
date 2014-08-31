
from selenium import webdriver
browser = webdriver.Firefox()

# Get the home page of our application:
browser.get('http://localhost:8000')

# Check for our initial code change - check To-Do appears in the title:
assert 'Django' in browser.title

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

# Close the browser now:
browser.quit()








