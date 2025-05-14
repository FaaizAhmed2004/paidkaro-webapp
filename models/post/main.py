@app.post("/posts/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts/", response_model=list[schemas.PostOut])
def get_all_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)

@app.get("/posts/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.get("/users/{user_id}/posts/", response_model=list[schemas.PostOut])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    return crud.get_posts_by_user(db, user_id)
