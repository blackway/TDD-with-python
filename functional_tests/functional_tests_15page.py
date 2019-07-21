from selenium import webdriver

browser = webdriver.Firefox()

assert 'To-Do' in browser.title

browser.quit()