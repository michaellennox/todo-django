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
        header_test = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )

        # She types "Buy peacock feathers" into a text box
        # That's one weird thing to type
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
            )

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
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
