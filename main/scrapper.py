import csv
import logging
import datetime

from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, \
    RemoteFilters

day = datetime.datetime.now().strftime("%b-%d")


def scrap(title, location):
    # Change root logger level (default is WARN)
    logging.basicConfig(level=logging.INFO)

    def on_data(data: EventData):
        data_all = [data.title, data.company, data.date, data.link]
        with open(f"{title}-{day}.csv", "w", encoding='UTF8', newline='') as r:
            writer = csv.writer(r)
            writer.writerow(data_all)

    def on_error(error):
        print('[ON_ERROR]', error)

    def on_end():
        print('[ON_END]')

    scraper = LinkedinScraper(
        chrome_executable_path=None,  # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
        chrome_options=None,  # Custom Chrome options here
        headless=True,  # Overrides headless mode only if chrome_options is None
        max_workers=1,
        # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
        slow_mo=10,  # Slow down the scraper to avoid 'Too many requests (429)' errors
    )

    # Add event listeners
    scraper.on(Events.DATA, on_data)
    scraper.on(Events.ERROR, on_error)
    scraper.on(Events.END, on_end)

    queries = [
        Query(
            query=f'{title}',
            options=QueryOptions(
                locations=[location],
                optimize=True,  # Block requests for resources like images and stylesheet
                limit=1000,  # Limit the number of jobs to scrape
                filters=QueryFilters(
                    # Filter by companies
                    relevance=RelevanceFilters.RECENT,
                    time=TimeFilters.MONTH,
                    type=[TypeFilters.FULL_TIME],
                    experience=[ExperienceLevelFilters.INTERNSHIP, ExperienceLevelFilters.ENTRY_LEVEL,
                                ExperienceLevelFilters.ASSOCIATE],
                )
            )
        ),
    ]

    scraper.run(queries)
