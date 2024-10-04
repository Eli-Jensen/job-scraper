import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from scrape_individual_job import JobScraper

print("Begin")
scraper = JobScraper()
print("Scraper initialized")

job_links = []
already_seen_counter = 0
page_number = 1
refresh_attempts = 0
max_refresh_attempts = 3 

try:
    scraper.driver.get("https://www.clearancejobs.com/jobs?loc=53,20,48&ind=nv&polygraph=p,l&limit=50")
    print(f"Getting all links from page {page_number}")

    while True:
        try:
            # Wait for the job links to be present
            WebDriverWait(scraper.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name'))
            )
            print(f"Got links from page {page_number}")

            # Get all job links from the current page
            page_job_links = [job.get_attribute('href') for job in scraper.driver.find_elements(By.CSS_SELECTOR, 'a.job-search-list-item-desktop__job-name')]
            page_job_links = list(set(page_job_links))
            
            for job_url in page_job_links:
                if not scraper.job_exists(job_url):
                    job_links.append(job_url)
                else:
                    already_seen_counter += 1
                    print(f"Already seen job: {job_url} (Count: {already_seen_counter})")
                    if already_seen_counter >= 5:
                        print("Encountered 5 already-seen jobs. Stopping the scrape.")
                        raise StopIteration

            # Check if the "Next" button is disabled (i.e., we are on the last page)
            try:
                # Refresh the page to close any popups or issues before interacting with "Next"
                print("Refreshing page before clicking the Next button.")
                scraper.driver.refresh()

                time.sleep(2)  # Allow time for page to reload after refreshing

                next_button = WebDriverWait(scraper.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn--next'))
                )
                
                scraper.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                time.sleep(1)
                next_button.click()

            except TimeoutException:
                print("Next button not found, assuming last page or unable to interact.")
                break
            except ElementNotInteractableException:
                print("Next button not interactable. Stopping scrape.")

            page_number += 1
            print(f"Moving to page {page_number}")
            refresh_attempts = 0
            time.sleep(1)

        except (ElementNotInteractableException, TimeoutException) as e:
            if refresh_attempts < max_refresh_attempts:
                refresh_attempts += 1
                print(f"Refreshing page due to issue: {e}. Attempt {refresh_attempts}/{max_refresh_attempts}")
                scraper.driver.refresh()
                time.sleep(3)
            else:
                print(f"Max refresh attempts ({max_refresh_attempts}) reached. Stopping scrape.")
                break

    # After collecting all job links, process each job page
    for job_url in job_links:
        print(f"Processing job_url {job_url}")
        try:
            scraper.driver.get(job_url)
            details = scraper.scrape_job_page(job_url)
            scraper.save_job_to_db(job_url, details)
        except Exception as e:
            print(f"Error processing job {job_url}: {e}")
        time.sleep(2)

except StopIteration:
    print("Scraping stopped based on stop conditions.")

except KeyboardInterrupt:
    print("Scraping interrupted by user.")

finally:
    scraper.close()
