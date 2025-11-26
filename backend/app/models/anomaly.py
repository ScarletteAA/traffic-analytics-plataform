from sqlalchemy import Column, UUID, String, DateTime, func
from app.database import Base

class Anomaly(Base):
    __tablename__ = "anomalies"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    description = Column(String)
    severity = Column(String)
    detected_at = Column(DateTime(timezone=True), server_default=func.now())