# --- job_crawler.py ---
import requests
from bs4 import BeautifulSoup
import time
import random


class JobCrawler:
    @staticmethod
    def fetch_jobs(url):
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            ])
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        jobs = []
        for job in soup.select('.job-card'):  # Replace with actual selectors
            title = job.select_one('.job-title').text
            company = job.select_one('.company-name').text
            location = job.select_one('.job-location').text
            description = job.select_one('.job-description').text
            skills = [skill.text for skill in job.select('.job-skills .skill')]

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "description": description,
                "skills": skills
            })

        return jobs

# Usage Example:
# jobs = JobCrawler.fetch_jobs('https://www.example.com/jobs')
# print(jobs)