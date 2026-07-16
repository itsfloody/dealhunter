from dealhunter.database.models import Base
from dealhunter.database.session import engine


def create_database():

    Base.metadata.create_all(
        engine
    )
