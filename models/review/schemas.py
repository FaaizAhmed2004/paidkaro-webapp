from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    product_id: int
    username: str
    rating: int
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int

    class Config:
        orm_mode = True
