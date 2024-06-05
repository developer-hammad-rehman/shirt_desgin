from app import settings
from sqlmodel import create_engine

connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg2"
)

engine = create_engine(url=connection_string , connect_args={"sslmode": "require"}, pool_recycle=300 , echo=True)