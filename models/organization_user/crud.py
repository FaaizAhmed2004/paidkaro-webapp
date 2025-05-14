def create_organization_user(db: Session, org_user: schemas.OrganizationUserCreate):
    db_org_user = models.OrganizationUser(**org_user.dict())
    db.add(db_org_user)
    db.commit()
    db.refresh(db_org_user)
    return db_org_user

def get_organization_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.OrganizationUser).offset(skip).limit(limit).all()

def get_organization_user_by_id(db: Session, user_id: int):
    return db.query(models.OrganizationUser).filter(models.OrganizationUser.id == user_id).first()
