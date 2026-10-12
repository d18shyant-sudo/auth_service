from fastapi import FastAPI
from auth_service.auth_routes.router import router
app = FastAPI()
app.include_router(router=router)