@app.post("/organization_users/", response_model=schemas.OrganizationUserOut)
def create_org_user(org_user: schemas.OrganizationUserCreate, db: Session = Depends(get_db)):
    return crud.create_organization_user(db=db, org_user=org_user)

@app.get("/organization_users/", response_model=list[schemas.OrganizationUserOut])
def read_org_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_organization_users(db=db, skip=skip, limit=limit)

@app.get("/organization_users/{user_id}", response_model=schemas.OrganizationUserOut)
def read_org_user(user_id: int, db: Session = Depends(get_db)):
    org_user = crud.get_organization_user_by_id(db, user_id)
    if not org_user:
        raise HTTPException(status_code=404, detail="User not found in organization")
    return org_user
