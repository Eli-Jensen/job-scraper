from sqlalchemy.orm import sessionmaker
from models import Job, Base
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class JobScraper:
    def __init__(self, driver_path='./chromedriver'):
        self.driver = webdriver.Chrome(driver_path)
        self.session = SessionLocal()
    
    def scrape_job_page(self, url):
        """Scrape job details from the page at the given URL."""
        self.driver.get(self.url)
        try:
            elem = self.driver.find_element(By.CLASS_NAME, "job-description-text")
            job_description = elem.text
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            job_description = None
        time.sleep(0.5)
        return job_description
    
    def job_exists(self, url):
        """Check if the job URL already exists in the database."""
        return self.session.query(Job).filter(Job.url == url).first() is not None

    def save_job_to_db(self, title, company_name, description, url):
        """Save a new job to the database."""
        new_job = Job(title=title, company_name=company_name, description=description, url=url)
        self.session.add(new_job)
        self.session.commit()

    def close(self):
        self.driver.quit()
        self.session.close()