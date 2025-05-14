@app.post("/organizations/", response_model=schemas.OrganizationOut)
def create_organization(org: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db=db, org=org)

@app.get("/organizations/", response_model=list[schemas.OrganizationOut])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_organizations(db=db, skip=skip, limit=limit)

@app.get("/organizations/{org_id}", response_model=schemas.OrganizationOut)
def read_organization(org_id: int, db: Session = Depends(get_db)):
    org = crud.get_organization_by_id(db, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org
