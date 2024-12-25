# Job and Profile Crawler API

## Introduction
This project crawls job postings and LinkedIn-like profiles, stores the data in a database, and provides APIs to retrieve relevant information.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database using `schema.sql`.
4. Run the API: `uvicorn api.app:app --reload`

## Endpoints
- `/profiles`: Fetch profiles based on designation, location, and company.
- `/jobs`: Fetch jobs based on skills and location.

## Scalability
- Database indexing.
- Load balancing with Gunicorn.
