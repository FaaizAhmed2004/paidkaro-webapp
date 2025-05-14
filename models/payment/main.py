# Add payment routes at the bottom of main.py

@app.post("/payments/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)

@app.get("/payments/", response_model=list[schemas.PaymentOut])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_payments(db, skip=skip, limit=limit)

@app.get("/payments/{payment_id}", response_model=schemas.PaymentOut)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
@app.put("/payments/{payment_id}", response_model=schemas.PaymentOut)
def update_payment(payment_id: int, payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = crud.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return crud.update_payment(db=db, payment=payment, payment_id=payment_id)
    