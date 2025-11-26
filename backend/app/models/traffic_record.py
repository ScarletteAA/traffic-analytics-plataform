from sqlalchemy import Column, UUID, ForeignKey, Integer, String, DateTime, func
from app.database import Base

class TrafficRecord(Base):
    __tablename__ = "traffic_records"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    point_id = Column(ForeignKey("monitor_points.id"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    vehicle_count = Column(Integer)
    creaeted_at = Column(DateTime(timezone=True), server_default=func.now())