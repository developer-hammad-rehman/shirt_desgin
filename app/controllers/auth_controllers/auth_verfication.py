from sqlmodel import Session, select
from app.models.users_model import Users
from app.controllers.auth_controllers.pwd_context import pwd_context, verifiy_hash_pass


def verfiy_email(session: Session, username: str):
    statment = select(Users).where(username == Users.username)
    result = session.exec(statment).first()
    return True if result else False


def verfiy_password(session: Session, username: str, plain_password: str):
    statment = select(Users).where(username == Users.username)
    result = session.exec(statment).first()
    return verifiy_hash_pass(
        plain_password=plain_password, hash_password=result.password
    )
