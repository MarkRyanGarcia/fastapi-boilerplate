# fastapi-boilerplate
boilerplate for fastapi API with SQLAlchemy and Clerk Auth


## Setup
1. Run these in order:
```
# Set up virtual environment
python3 -m venv .venv

# Activate venv
source .venv/bin/activate

pip install -r requirements.txt
```

2. Put this in root directory:
/.env
```
DEBUG="true"
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
CLERK_SECRET_KEY=sk_live...  # Optional if you want clerk auth
```

3. Run command:
`fastapi dev app`


## Database Migrations
Only do this when you change the database models / tables
1. Make necessary changes in `/app/db/models/...`
2. Import model in `/app/db/models/__init__.py`
3. Generate a migration revision:
    `alembic revision --autogenerate -m "{revision message}"
4. Verify changes in `/alembic/versions/...`
5. Migrate database changes: `alembic upgrade head`