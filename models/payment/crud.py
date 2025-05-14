# Add this to the bottom of crud.py

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Payment).offset(skip).limit(limit).all()

def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()

def update_payment(db: Session, payment_id: int, payment: schemas.PaymentCreate):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if db_payment:
        for key, value in payment.dict().items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment
def delete_payment(db: Session, payment_id: int):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment
def get_payments_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Payment).filter(models.Payment.user_id == user_id).offset(skip).limit(limit).all()
def get_payment_by_reference(db: Session, reference: str):
    return db.query(models.Payment).filter(models.Payment.reference == reference).first()
def get_payments_by_status(db: Session, status: str, skip: int = 0, limit: int = 10):
    return db.query(models.Payment).filter(models.Payment.status == status).offset(skip).limit(limit).all()
def get_payments_by_method(db: Session, method: str, skip: int = 0, limit: int = 10):
    return db.query(models.Payment).filter(models.Payment.method == method).offset(skip).limit(limit).all()
def get_payments_by_date(db: Session, start_date: str, end_date: str, skip: int = 0, limit: int = 10):
    return db.query(models.Payment).filter(models.Payment.created_at >= start_date, models.Payment.created_at <= end_date).offset(skip).limit(limit).all()
def get_payment_count(db: Session):
    return db.query(models.Payment).count()
def get_payment_sum(db: Session):
    return db.query(func.sum(models.Payment.amount)).scalar()