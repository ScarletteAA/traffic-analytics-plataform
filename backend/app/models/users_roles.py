from sqlalchemy import Column, ForeignKey
from app.database import Base


class UsersRoles(Base):
    __tablename__= "users_roles"

    user_id = Column(ForeignKey("users.id"), primary_key=True)
    role_id = Column(ForeignKey("roles.id"), primary_key=True)