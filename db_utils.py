# --- db_utils.py ---
import psycopg2
from psycopg2.extras import Json

connection = psycopg2.connect(
    host="localhost",
    database="Linkedln_Project",
    user="anikr04",
    password="password",  # Replace with verified password
    port=5432
)


def fetch_profiles_from_db(designation, location, company):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM profiles 
            WHERE title = %s AND location = %s AND company = %s
            """,
            (designation, location, company)
        )
        return cursor.fetchall()

def fetch_jobs_from_db(skills, location):
    with connection.cursor() as cursor:
        query = "SELECT * FROM jobs WHERE location = %s"
        params = [location]

        if skills:
            query += " AND skills && %s"
            params.append(skills)

        cursor.execute(query, params)
        return cursor.fetchall()
