from app.models.store import Store

def create_store(store:Store):
    return{"message":"Store created successfully",
           "store":store}