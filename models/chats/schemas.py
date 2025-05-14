from datetime import datetime

class ChatBase(BaseModel):
    sender_id: int
    receiver_id: int
    message: str

class ChatCreate(ChatBase):
    pass

class ChatOut(ChatBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
