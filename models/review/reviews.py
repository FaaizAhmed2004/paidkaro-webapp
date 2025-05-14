from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Text
from database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    username = Column(String(50), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
