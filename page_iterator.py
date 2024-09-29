import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrape_individual_job import JobScraper

# Initialize the scraper
print("Begin")
scraper = JobScraper()
print("Scraper initialized")

try:
    scraper.driver.get("https://www.clearancejobs.com/jobs?loc=53,48,20&ind=nv&polygraph=p,l")
    print("Getting all links")
    
    # Wait for the job links to be present
    WebDriverWait(scraper.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name'))
    )
    print("Got links")

    job_links = scraper.driver.find_elements(By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name')

    for index, job_link in enumerate(job_links):
        job_url = job_link.get_attribute('href')
        print(f"Considering job_url {job_url}")

        if not scraper.job_exists(job_url):
            try:
                job_links[index].click()

                details = scraper.scrape_job_page(job_url)

                scraper.save_job_to_db(job_url, details)

            except Exception as e:
                print(f"Error processing job {job_url}: {e}")


            scraper.driver.back()
            time.sleep(3)  # Wait for the page to reload

            WebDriverWait(scraper.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name'))
            )
            job_links = scraper.driver.find_elements(By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name')

except KeyboardInterrupt:
    print("Scraping interrupted by user.")

finally:
    scraper.close()
