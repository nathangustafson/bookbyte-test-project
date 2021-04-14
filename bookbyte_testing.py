import json
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from urllib.request import urlopen


class TestRequest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Check that our street address is correct on amazon seller
    # profile - https://www.amazon.com/sp?seller=A2N51X1QYGFUPK
    # 2800 Pringle Rd SE Suite 100
    def test_amazon_seller_street_address(self):

        # Arrange
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.amazon.com/sp?seller=A2N51X1QYGFUPK")
        search_term = "2800 Pringle Rd SE Suite 100"

        # Act
        index_of_text = self.driver.page_source.find(search_term)

        # Assert
        self.assertGreater(index_of_text, -1, "The text '" + search_term + "' does not exist in the page source")

    # Verify our search bar works by searching for 'college'
    # books https://www.bookbyte.com/advancedsearch.aspx
    def test_that_bookbyte_search_returns_results_page(self):

        # Arrange
        self.driver.get("https://www.bookbyte.com/advancedsearch.aspx")
        search_term = "college"
        title_to_match = "You searched for the keyword: " + search_term

        # Act
        # NOTE: no 'wait.until' used as .aspx web forms are reloading the page and not loading through an ajax call.
        self.driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbKeywords").send_keys(search_term + Keys.RETURN)
        title = self.driver.title

        # Assert
        self.assertEqual(title, title_to_match, "The destination page did not include the expected title.")

    # Using the Google Books API Verify "Brian W. Kernighan", and "Dennis M. Ritchie"
    # are the authors of The C Programming Language (Hint: the isbn for this book is 0131103628)
    # https://developers.google.com/books/docs/v1/using
    def test_for_expected_authors_in_google_book_api_query(self):

        # Arrange
        authors_to_test = ["Brian W. Kernighan", "Dennis M. Ritchie"]
        api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        isbn = "0131103628"

        # Act
        # send a request and get a JSON response
        resp = urlopen(api + isbn)
        # parse JSON into Python as a dictionary
        book_data = json.load(resp)
        # create additional variables for easy querying
        volume_info = book_data["items"][0]["volumeInfo"]
        authors = volume_info["authors"]

        # Assert
        # Note: This test will only pass if the authors pulled from the Google Books API are
        #        listed in the same order as the authors_to_test list.
        self.assertEqual(authors, authors_to_test, "The book's authors do not match what was expected.")


if __name__ == '__main__':
    unittest.main()
    # print ("all done tests ran" )