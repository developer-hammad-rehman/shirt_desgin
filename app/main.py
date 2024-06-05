from fastapi import FastAPI
from app.db.create_table import create_tables
from app.models.orders_model import Orders
from app.models.users_model import Users
from contextlib import asynccontextmanager
from app.health_routes.api import health_router
from app.auth_api.routes import auth_router
from app.orders_api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(title="Tee cheap Backend", lifespan=lifespan)


app.include_router(health_router, prefix="/health", tags=["Health routes"])


@app.get("/", tags=["Root Route"])
def root_route():
    return {"messaage": "Welcome to the server of tee cheap"}


app.include_router(auth_router, tags=["Auth Apis"])


app.include_router(router, tags=["Orders"])
