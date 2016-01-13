from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. 
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # Well I guess were doing a todo....
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box
        # That's one weird thing to type

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"

        # Surprisingly! The page updates again and has BOTH items
        # oh gosh golly

        # She wonders whether the site remembers this or whether it's crap
        # Oh look! She has a unique URL for just herself
        # And there's some text to tell her about it

        # Now she goes to the URL and oh gosh darn what do you know
        # the to-do list is still there!

        # I wonder if that was magic or just an awesome programmer called Michael
        # (who really should get hired by someone if they've bothered reading this)
        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
