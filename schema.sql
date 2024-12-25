# --- schema.sql ---
-- Jobs Table
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(255),
    skills TEXT[],
    description TEXT
);

-- Profiles Table
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    title VARCHAR(255),
    location VARCHAR(255),
    company VARCHAR(255),
    skills TEXT[]
);
