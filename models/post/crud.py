def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).filter(models.Post.is_active == True).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts_by_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.user_id == user_id).all()
