from selenium import webdriver
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title, "Browser title was" + browser.title
