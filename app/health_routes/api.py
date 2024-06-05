from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/")
def health_root_route():
    return {"Working" : 'Correct'}


@health_router.get('/status')
def health_status_route():
    return {"status" : "Ok"} 