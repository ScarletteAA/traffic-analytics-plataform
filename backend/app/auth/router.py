
from http.client import HTTPException
from app.auth.utils import create_access_token, hash_password, verify_password
from app.models.user import User
from app.database import get_db
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    user_exist = db.query(User).filter(User.email == user.email).first()
    if user_exist:
        raise HTTPException(400, "Email already registered")
    hashed_password = hash_password(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

@router.post("/login")
async def login():
    user = db.query(User).filter(User.email == user.email).first()
    if not user or not verify_password(user.password, user.hashed_password):
        raise HTTPException(400, "Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
