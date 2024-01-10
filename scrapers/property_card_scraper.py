import ast
import re
from bs4 import BeautifulSoup

from settings import CONVERT_IMAGES_TO_BIGGER_SIZE


class PropertyCardScraper:
    @staticmethod
    def get_text_from_tag(tag: BeautifulSoup) -> str:
        return tag.text.strip() if tag else None

    def get_property_title(self, soup: BeautifulSoup) -> str:
        return self.get_text_from_tag(soup.find("span", {"data-id": "PageTitle"}))

    def get_property_address(self, soup: BeautifulSoup) -> str:
        return self.get_text_from_tag(soup.find("h2", {"itemprop": "address"}))

    @staticmethod
    def get_property_region(address: str) -> str:
        return address.split(", ", 1)[1] if address else None

    def get_property_description(self, soup: BeautifulSoup) -> str:
        return self.get_text_from_tag(soup.find("div", {"itemprop": "description"}))

    def get_property_price(self, soup: BeautifulSoup) -> int:
        price = self.get_text_from_tag(soup.find_all("span", {"class": "text-nowrap"})[1])
        numbers = "".join(re.findall(r"\d+", price))
        return int(numbers)

    def get_property_rooms(self, soup: BeautifulSoup) -> int:
        bedrooms = self.get_text_from_tag(soup.find("div", {"class": "col-lg-3 col-sm-6 cac"}))
        bathrooms = self.get_text_from_tag(soup.find("div", {"class": "col-lg-3 col-sm-6 sdb"}))

        def get_number_of_rooms(rooms: str) -> int | None:
            return int(rooms.strip().split()[0]) if rooms else 0

        return sum(map(get_number_of_rooms, (bedrooms, bathrooms)))

    def get_property_square(self, soup: BeautifulSoup) -> int:
        all_features_info = soup.find_all("div", {"class": "carac-value"})

        for data in all_features_info:
            try:
                return int(
                    self.get_text_from_tag(data).split()[0].replace(",", "")
                )
            except ValueError:
                continue

    @staticmethod
    def get_property_images(soup: BeautifulSoup) -> list[str]:
        images = str(soup.find("div", {"class": "thumbnail last-child first-child"}))

        def convert_size(img_links: str) -> str:
            if CONVERT_IMAGES_TO_BIGGER_SIZE:
                return img_links.replace(
                    "w=320&h=240", "w=1024&h=1024"
                ).replace("w=640&h=480", "w=1024&h=1024")
            return img_links

        return ast.literal_eval(
            convert_size(re.findall(r"\[.*]", images)[0])
        )
