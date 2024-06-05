from fastapi import APIRouter, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from typing import Annotated
from app.controllers.auth_controllers.auth_verfication import verfiy_email , verfiy_password
from app.controllers.auth_controllers.pwd_context import create_hash
from app.db.get_session import DBSESSION 
from app.controllers.auth_controllers.jwt_token import generate_access_token ,  generate_refresh_token , decode_refresh_token
from app.models.users_model import Users


auth_router = APIRouter()


@auth_router.post('/auth')
def auth_route(formdata : Annotated[OAuth2PasswordRequestForm , Depends()] , session  : DBSESSION , response  : Response):
    is_email = verfiy_email(session=session , username=formdata.username)
    if is_email:
        is_passord = verfiy_password(session=session  , username=formdata.username , plain_password=formdata.password)
        if is_passord:
            access_token = generate_access_token({"username":formdata.username})
            refresh_token = generate_refresh_token({"username":formdata.username})
            response.set_cookie(key="access_token" ,  value=access_token)
            response.set_cookie(key="refresh_token" , value=refresh_token)
            return {"access_token" : access_token , "token_type":"bearer"}
        else:
            raise HTTPException(detail="Password is incorrect" , status_code=404)
    else:
        raise HTTPException(detail="Email donot Exist" , status_code=404)
    
@auth_router.post("/register")
def register_route(formdata : Annotated[OAuth2PasswordRequestForm , Depends()] ,  session:DBSESSION):
    is_email = verfiy_email(session=session , username=formdata.username)
    if is_email:
         raise HTTPException(detail="Email  Exist" , status_code=404)
    else:
        hash_password = create_hash(formdata.password)
        data = Users(username=formdata.username , password=hash_password)
        session.add(data)
        session.commit()
        session.refresh(data)
        return data
    

@auth_router.get('/oauth2-access_token')
def create_access_token_route(refresh_token : str = Depends(decode_refresh_token)):
    username = refresh_token["username"]
    access_token  = generate_access_token(data={"username" : username})
    return {"access_token" : access_token}