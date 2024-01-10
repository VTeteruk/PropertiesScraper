import logging

from scrapers.properties_scraper import PropertiesScraper
from settings import configure_logging, RESULTS_FILE_SETTINGS
from utilities.saver import save_dataclass_list_to_json

configure_logging()


def main() -> None:
    with PropertiesScraper() as scraper:
        logging.info("Scrape properties links...")
        properties_links = scraper.scrape_properties_links()

    logging.info("Scrape properties...")
    properties = scraper.scrape_properties(properties_links)

    logging.info("Saving data to json...")
    save_dataclass_list_to_json(properties, RESULTS_FILE_SETTINGS)

    logging.info("Data were saved successfully")


if __name__ == "__main__":
    main()
