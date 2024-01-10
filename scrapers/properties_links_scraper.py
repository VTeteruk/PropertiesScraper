import time

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from scrapers.chrome_scraper import ChromeScraper
from settings import BASE_URL, MAX_AMOUNT_OF_PROPERTIES


class PropertiesLinksScraper(ChromeScraper):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def extract_link_from_web_element(element: WebElement) -> str:
        return element.get_attribute("href")

    def get_properties_links(self) -> list[str]:
        return [
            self.extract_link_from_web_element(element)
            for element
            in self.driver.find_elements(By.XPATH, "//a[@class='property-thumbnail-summary-link']")
        ]

    def next_page(self) -> None:
        self.driver.find_element(By.XPATH, "//li[@class='next']/a").click()

    def is_last_page(self) -> bool:
        try:
            self.driver.find_element(By.XPATH, "//li[@class='next inactive']")
            return True
        except NoSuchElementException:
            return False

    def scrape_properties_links(self) -> list:
        self.driver.get(BASE_URL + "en/properties~for-rent")

        properties_links = []

        while len(properties_links) < MAX_AMOUNT_OF_PROPERTIES:
            # To be sure that all cards were loaded
            time.sleep(0.15)
            try:
                properties_links += self.get_properties_links()
            except StaleElementReferenceException:
                continue

            if self.is_last_page():
                break

            self.next_page()

        return properties_links[:MAX_AMOUNT_OF_PROPERTIES]
