from pydantic import BaseModel
from pydantic import Field

class Accounts(BaseModel):
    account_number: str
    user_id: str
    balance: float = Field(default=0.0)
    account_type: str 
    status: str
    initial_deposit: float
