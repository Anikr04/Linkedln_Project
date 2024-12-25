# --- test_api.py ---
import pytest
from fastapi.testclient import TestClient
from Api.app import app

client = TestClient(app)

def test_get_profiles():
    response = client.get("/profiles?designation=developer&location=NY&company=Google")
    assert response.status_code == 200


def test_get_jobs():
    response = client.get("/jobs?skills=Python&location=NY")
    assert response.status_code == 200

# --- test_crawlers.py ---
from Crawlers.job_crawler import JobCrawler
from Crawlers.profile_crawler import ProfileCrawler

def test_job_crawler():
    jobs = JobCrawler.fetch_jobs("https://example.com/jobs")
    assert len(jobs) > 0

def test_profile_crawler():
    profiles = ProfileCrawler.fetch_profiles("https://example.com/profiles")
    assert len(profiles) > 0

