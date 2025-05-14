@app.post("/projects/", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)

@app.get("/projects/", response_model=list[schemas.ProjectOut])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)

@app.get("/projects/{project_id}", response_model=schemas.ProjectOut)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
@app.put("/projects/{project_id}", response_model=schemas.ProjectOut)
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_id(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(db=db, project=project, project_id=project_id)