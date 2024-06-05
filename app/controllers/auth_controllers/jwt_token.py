from fastapi import HTTPException
from jose import JWTError, jwt
from datetime import timedelta, datetime, timezone
from app.settings import ALGORITHM, SECRET_KEY


def generate_access_token(data: dict[str, str]):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    jwt_token = jwt.encode(to_encode, key=str(SECRET_KEY), algorithm=str(ALGORITHM))
    return jwt_token


def generate_refresh_token(data: dict[str, str]):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=1)
    to_encode.update({"exp": expire})
    jwt_token = jwt.encode(to_encode, key=str(SECRET_KEY), algorithm=str(ALGORITHM))
    return jwt_token


def decode_refresh_token(token: str):
    try:
        decode_token = jwt.decode(token, key=str(SECRET_KEY), algorithms=str(ALGORITHM))
        return decode_token
    except JWTError as je:
        raise HTTPException(status_code=404, detail=str(je))
