import time
import schedule

from dawn_scraper import scraper_dawn
from ummat_scraper import scraper_ummat

def run_pipeline():
    print("Starting scheduling pipeline...")

    scraper_dawn()
    scraper_ummat()

    print("Scraping complete!")

# run every 6 hours
schedule.every(1).minutes.do(run_pipeline)

print("Scheduler started...")

run_pipeline()

while True:
    schedule.run_pending()
    time.sleep(60)