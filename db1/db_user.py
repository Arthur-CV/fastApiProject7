from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db1.models import Db1User


def create_user(db1: Session, request: UserBase):
  new_user = Db1User(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db1.add(new_user)
  db1.commit()
  db1.refresh(new_user)
  return new_user