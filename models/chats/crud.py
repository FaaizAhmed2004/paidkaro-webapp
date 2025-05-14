def send_message(db: Session, chat: schemas.ChatCreate):
    db_chat = models.Chat(**chat.dict())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_conversation(db: Session, user1_id: int, user2_id: int):
    return db.query(models.Chat).filter(
        ((models.Chat.sender_id == user1_id) & (models.Chat.receiver_id == user2_id)) |
        ((models.Chat.sender_id == user2_id) & (models.Chat.receiver_id == user1_id))
    ).order_by(models.Chat.timestamp).all()
