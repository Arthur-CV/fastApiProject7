from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db1.database import get_db1
from db1 import db1_user


router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db1: Session = Depends(get_db1)):
  return db1_user.create_user(db1, request)

# Read user

# Update user

# Delete user