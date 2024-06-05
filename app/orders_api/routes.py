from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.db.get_session import DBSESSION
from app.models.orders_model import Orders
from app.controllers.ouath2_schema.oauth2_schema import oauth2_schema
from jose import jwt , JWTError
from app.settings import SECRET_KEY , ALGORITHM

router  = APIRouter()



@router.post('/place-order')
def order_route(order:Orders , session:DBSESSION , token : Annotated[str , Depends(oauth2_schema)]):
 try:
    decode_token = jwt.decode(token , key=str(SECRET_KEY) , algorithms=str(ALGORITHM))
    session.add(order)
    session.commit()
    session.refresh(order)
    return order
 except JWTError as je:
   raise HTTPException(status_code=404 , detail=str(je))


@router.get('/get-order/{id}')
def get_order(id : int,token : Annotated[str , Depends(oauth2_schema)] , session:DBSESSION):
  try:
    decode_token = jwt.decode(token , key=str(SECRET_KEY) , algorithms=str(ALGORITHM))
    result = session.exec(select(Orders).where(id == Orders.user_id)).all()
    return result
  except JWTError as je:
   raise HTTPException(status_code=404 , detail=str(je))