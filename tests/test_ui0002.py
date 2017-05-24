# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()
import unittest
import os
from selenium import webdriver

test_id = 'uitest0002'
tmp = 'tmp/'
DIRNAME = os.path.dirname(os.path.abspath(__file__))
if os.path.isdir(DIRNAME+'/'+tmp) == False:
    os.mkdir(DIRNAME+'/'+tmp)

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), tmp+test_id + ".png")

class uitest0002(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_uitest0002(self):
        browser = self.browser
        browser.set_window_size(1280, 1280)
        browser.get('http://localhost:8000/admin')
        browser.find_element_by_id("id_username").send_keys("jintaka")
        browser.find_element_by_id("id_password").send_keys("pa$$word")
        browser.find_element_by_class_name("submit-row").click()
        home_link = browser.find_element_by_link_text('サイトを表示')
        home_link.click()
        browser.save_screenshot(FILENAME)
        expected = 'Django Tutorial blog'

        print("==TestResult=========================")
        if browser.title == expected:
            print("OK!")
            print('Expected:'+expected)
            print('Result  :'+browser.title)
        else:
            print("NG")
            print('Expected:'+expected)
            print('Result     :'+browser.title)
        print("=====================================")
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
