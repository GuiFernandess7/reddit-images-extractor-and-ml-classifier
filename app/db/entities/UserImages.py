from sqlalchemy import Column, BigInteger, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import enum

Base = declarative_base()

class Gender(enum.Enum):
    M = 'M'
    F = 'F'

class UserImages(Base):
    __tablename__ = 'user_images'

    ts = Column(BigInteger, primary_key=True)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    sex = Column(Enum(Gender), nullable=True)
    subreddit = Column(String, nullable=True)

    def __repr__(self):
        return (f"<UserImages(ts={self.ts}, image_url='{self.image_url}', "
                f"created_at={self.created_at}, sex='{self.sex}')>, subreddit='{self.subreddit}')>")
