from sqlalchemy import Column, UUID, String
from app.database import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String)