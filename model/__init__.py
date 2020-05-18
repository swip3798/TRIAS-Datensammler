import vvar

# Import all model classes
from .stop import Stop

# Import base
from .base import Base

# Import sqlalchemy shit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to database
engine = create_engine(vvar.env.sqlurl, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()