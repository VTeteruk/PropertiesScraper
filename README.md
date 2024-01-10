# Properties Scraper
## Overview
This Python web scraper is designed to collect information about real estate properties from a specific website (https://realtylink.org/). The scraper is divided into several modules, each responsible for a specific aspect of the scraping process.
___
## Requirements
1. [Python 3.x](https://www.python.org/downloads/) must be installed.
2. Clone the repository:
    ```bash
    git clone https://github.com/VTeteruk/PropertiesScraper.git
    ```
3. Create and activate your virtual environment:
   * For Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate.bat
     ```
4. Install the required Python libraries using the following command:
   ```bash
   pip install -r requirements.txt
___
## Usage
Run the script using the following command:

```bash
python main.py
```

The script will create a JSON file inside results folder with scraped data.
___
## Settings
You can customize the script behavior by modifying the settings in the `settings.py` file.

**NOTE:**

* `HEADLESS = True` - allows you to hide the browser.
___
