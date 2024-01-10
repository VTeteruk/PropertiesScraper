import logging
from os import path

# Base urls settings
BASE_URL = "https://realtylink.org/"

# Driver settings
HEADLESS = False
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Scraper settings
MAX_AMOUNT_OF_PROPERTIES = 60
CONVERT_IMAGES_TO_BIGGER_SIZE = True
RESULTS_FILE_SETTINGS = path.join("results", "data.json")


# Logging settings
def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )
