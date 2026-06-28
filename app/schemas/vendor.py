from pydantic import BaseModel


class Vendor(BaseModel):
    vendor_id: str
    vendor_name: str
    vendor_email: str
    vendor_phone: str
    vendor_type: str
    supported_states: str