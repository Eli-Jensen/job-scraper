from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from dotenv import load_dotenv
import time
from collections import defaultdict
from models import Job

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No DATABASE_URL environment variable found")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class JobScraper:
    def __init__(self, driver_path=None):
        # Set up Chrome options
        chrome_options = Options()
        
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--window-size=1920x1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        print("Scraper initialized in full browser mode")
        self.session = SessionLocal()

    def scrape_job_page(self, url):
        """Scrape job details from the page at the given URL."""
        self.driver.get(url)
        details = defaultdict(str)

        try:
            # Scrape each element as soon as it is available
            details["job_title"] = self.wait_for_element(By.CLASS_NAME, 'job-name', 10) or "No title available"
            print(f"Job title found: {details['job_title']}")

            details["job_description"] = self.wait_for_element(By.CLASS_NAME, "job-description-text", 10) or "No description available"
            print(f"Job description found: {details['job_description'][0:100]}")

            details["company_name"] = self.wait_for_element(By.CLASS_NAME, 'job-location', 10) or "No company name available"
            print(f"Company name found: {details['company_name']}")

            details["job_location"] = self.wait_for_element(By.CLASS_NAME, 'job-view__location-name', 10) or "No location available"
            print(f"Job location found: {details['job_location']}")

        except Exception as e:
            print("Error scraping the job page:", e)

        return details

    def wait_for_element(self, by, value, timeout=10):
        """Helper function to wait for an element to be present and return its text."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element.text if element else None
        except TimeoutException:
            print(f"Element with {by}='{value}' not found within {timeout} seconds")
            return None

    def job_exists(self, url):
        """Check if the job URL already exists in the database."""
        return self.session.query(Job).filter(Job.url == url).first() is not None

    def save_job_to_db(self, url, details: dict):
        """Save a new job to the database if all required details are present."""
        required_fields = ['job_title', 'company_name', 'job_description', 'job_location']
        if all(details.get(field) for field in required_fields):
            try:
                new_job = Job(
                    title=details['job_title'],
                    company_name=details['company_name'],
                    description=details['job_description'],
                    url=url,
                    location=details['job_location']
                )
                self.session.add(new_job)
                self.session.commit()
                print(f"Job saved: {details['job_title']} at {details['company_name']}")
            except Exception as e:
                print(f"Error saving job to the database: {e}")
                self.session.rollback()
        else:
            print(f"Skipping job {url} due to missing required details {details}")

    def close(self):
        """Close the browser and the database session."""
        self.driver.quit()
        self.session.close()