# --- app.py ---
from fastapi import FastAPI, Query
from typing import List
from Data_Base.db_utils import fetch_profiles_from_db, fetch_jobs_from_db

app = FastAPI()

@app.get("/profiles")
def get_profiles(designation: str, location: str, company: str):
    profiles = fetch_profiles_from_db(designation, location, company)
    return {"profiles": profiles}

@app.get("/jobs")
def get_jobs(skills: List[str] = Query(None), location: str = None):
    jobs = fetch_jobs_from_db(skills, location)
    return {"jobs": jobs}
