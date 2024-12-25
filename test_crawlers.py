# --- test_crawlers.py ---
from Crawlers.job_crawler import JobCrawler
from Crawlers.profile_crawler import ProfileCrawler

def test_job_crawler():
    jobs = JobCrawler.fetch_jobs("https://example.com/jobs")
    assert len(jobs) > 0

def test_profile_crawler():
    profiles = ProfileCrawler.fetch_profiles("https://example.com/profiles")
    assert len(profiles) > 0