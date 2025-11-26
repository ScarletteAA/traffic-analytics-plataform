from sqlalchemy import Boolean, Column, UUID, DateTime, String, Float, func
from app.database import Base

class MonitorPoint(Base):
    __tablename__ = "monitor_points"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())