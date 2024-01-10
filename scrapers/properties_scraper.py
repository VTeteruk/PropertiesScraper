import asyncio

import aiohttp
from bs4 import BeautifulSoup

from models.models import Property
from scrapers.properties_links_scraper import PropertiesLinksScraper
from scrapers.property_card_scraper import PropertyCardScraper
from settings import USER_AGENT


class PropertiesScraper(PropertiesLinksScraper, PropertyCardScraper):
    @staticmethod
    async def fetch_url_content(session, url: str) -> str:
        async with session.get(url) as response:
            return await response.text()

    def get_property_data(self, soup: BeautifulSoup) -> dict:
        address = self.get_property_address(soup)
        return {
            "title": self.get_property_title(soup),
            "address": address,
            "region": self.get_property_region(address),
            "description": self.get_property_description(soup),
            "images": self.get_property_images(soup),
            "price": self.get_property_price(soup),
            "rooms": self.get_property_rooms(soup),
            "square": self.get_property_square(soup),
        }

    async def create_property_instance(self, session, property_link: str) -> Property:
        text_response = await self.fetch_url_content(session, property_link)
        soup = BeautifulSoup(text_response, "html.parser")

        property_data = self.get_property_data(soup)
        return Property(
            url=property_link,
            **property_data
        )

    async def create_coroutines(self, properties_links: list[str]) -> list[Property]:
        headers = {"user-agent": USER_AGENT}

        async with aiohttp.ClientSession(headers=headers) as session:
            coroutines = [
                self.create_property_instance(session, property_link)
                for property_link
                in properties_links
            ]
            result = await asyncio.gather(*coroutines)
        return result

    def scrape_properties(self, properties_links: list[str]) -> list[Property]:
        return asyncio.run(self.create_coroutines(properties_links=properties_links))
