from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_hash(password : str):
    return pwd_context.hash(password)


def verifiy_hash_pass(plain_password : str , hash_password : str):
    return pwd_context.verify(plain_password , hash_password)