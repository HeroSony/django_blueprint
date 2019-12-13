# Scaffold Django Project

### Drop All Tables
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

### Avoiding create new user and group depends on their corporate account

### Postgres Command
\l List all databases
sudo -u postgres psql
    # Create New Database
        CREATE DATABASE test;
        CREATE USER test WITH PASSWORD '!@#$%herovirak';
        ALTER ROLE test SET client_encoding TO 'utf-8';
        ALTER ROLE test SET default_transaction_isolation TO 'read committed';
        ALTER ROLE test SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE test to test;

# Recruitment Officer
CA_PEOPLE & CA_CANDIDATE

# How to reset the primary key sequence in PostgreSQL with Django
python manage.py sqlsequencereset ca_people | python manage.py dbshell
python manage.py sqlsequencereset ca_structured_entity | python manage.py dbshell