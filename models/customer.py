from pydantic import BaseModel

class Customer(BaseModel):
    user_name:   str
    user_id:     str
    active_accounts: list
    
