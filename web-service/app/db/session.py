# Session connect to database
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from settings import config

data = config.DATABASE_URL

engine = create_engine(data, pool_pre_ping=True, echo=True)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

