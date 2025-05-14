# Add this to the bottom of schemas.py

from pydantic import Field

class PaymentBase(BaseModel):
    user_id: int
    amount: float
    method: str
    status: str = Field(default="pending")
    reference: str | None = None

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        allow_population_by_field_name = True       
        use_enum_values = True
        anystr_strip_whitespace = True
        anystr_lower = True
        anystr_upper = True 
        min_anystr_length = 1
        max_anystr_length = 255
      