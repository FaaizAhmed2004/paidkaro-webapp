class PostBase(BaseModel):
    user_id: int
    title: str
    description: str
    budget: float | None = None
    is_active: bool = True

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
