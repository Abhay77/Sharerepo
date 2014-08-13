from selenium import webdriver
from wikiaweb import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Wikiatest(unittest.TestCase):
    def setUp(self):
        val1 = readconf()
        val2 = conftodict(val1)
        username = val2['username']
        password = val2['password']
        self.wikia = WikiaGUI(username, password, url) 
  
    def test_wikia(self):
        self.wikia.login()

    def tearDown(self):
        self.wikia.quit()
        

if __name__ == "__main__":
    unittest.main()
