from pydantic import BaseModel

class Store( BaseModel):
    store_id: str
    store_name: str
    address: str
    city: str
    state: str
    zip_code: str
    contact_name: str
    contact_email: str
    contact_number: str