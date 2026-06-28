from sqlalchemy.orm import Session

from app.schemas.store import Store
from app.database.models.stotre import StoreDB


def create_store(store: Store, db: Session):

    db_store = StoreDB(
        store_id=store.store_id,
        store_name=store.store_name,
        address=store.address,
        city=store.city,
        state=store.state,
        zip_code=store.zip_code,
        contact_name=store.contact_name,
        contact_email=store.contact_email,
        contact_number=store.contact_number
    )

    db.add(db_store)

    db.commit()

    db.refresh(db_store)

    return {
        "message": "Store created successfully",
        "store": db_store
    }