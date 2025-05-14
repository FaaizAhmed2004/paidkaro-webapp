@app.post("/chats/", response_model=schemas.ChatOut)
def send_chat(chat: schemas.ChatCreate, db: Session = Depends(get_db)):
    return crud.send_message(db=db, chat=chat)

@app.get("/chats/conversation/", response_model=list[schemas.ChatOut])
def get_chat_conversation(user1_id: int, user2_id: int, db: Session = Depends(get_db)):
    return crud.get_conversation(db, user1_id=user1_id, user2_id=user2_id)
