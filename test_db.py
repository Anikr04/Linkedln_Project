# --- test_db.py ---
from Data_Base.db_utils import fetch_profiles_from_db, fetch_jobs_from_db

def test_fetch_profiles_from_db():
    profiles = fetch_profiles_from_db("developer", "NY", "Google")
    assert len(profiles) >= 0

def test_fetch_jobs_from_db():
    jobs = fetch_jobs_from_db(["Python", "SQL"], "NY")
    assert len(jobs) >= 0