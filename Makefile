
# Make Development Project Using These Command one by one

development:
   poetry new app 
   poetry install fastapi openai "uvicorn[standard]" python-jose passlib[bycrpt] sqlmodel psycopg2
   poetry run uvicorn app.main:app --reload