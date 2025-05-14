from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Add this to the bottom of models.py

from sqlalchemy import Float, ForeignKey

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="pending")  # pending, completed, failed
    method = Column(String(30), nullable=False)  # e.g., "credit_card", "paypal"
    reference = Column(String(100), nullable=True)  # transaction ID or reference
    created_at = Column(String(50), nullable=False)  # timestamp of payment creation
    updated_at = Column(String(50), nullable=False)  # timestamp of last update
    user = relationship("User", back_populates="payments")
    # Assuming you have a User model defined elsewhere