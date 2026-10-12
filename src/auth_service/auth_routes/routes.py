from fastapi import APIRouter
from fastapi.responses import JSONResponse
from auth_service.auth_services.service import AuthService
from auth_service.auth_schemas.schema import SignUp,Login
from auth_service.config.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
import logging
logging.basicConfig(level=logging.INFO)
router = APIRouter()


@router.post("/sign_up")
async def sign_up(data: SignUp,db:AsyncSession = Depends(get_db)):
    try:
        result = await AuthService.store_account(db=db,userdata=data)
        return JSONResponse(
            status_code=201,
            content={
                "message": "Account created successfully"
            }
        )

    except ValueError:
        return JSONResponse(
            status_code=409,
            content={
                "message": "Username or email already exists"
            }
        )

    except Exception as e:
        logging.exception("Error: %s",e)
        
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal server error"
            }
        )
@router.post("/login")
async def login(
    data: Login,
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await AuthService.verify_user(
            db=db,
            userdata=data,
        )

        if result:
            return JSONResponse(
                status_code=200,
                content={
                    "token":result,
                    "message": "User authenticated successfully",
                    "authenticated": True,
                },
            )

        return JSONResponse(
            status_code=401,
            content={
                "message": "Invalid email or password",
                "authenticated": False,
            },
        )

    except Exception as e:
        logging.exception("Error: %s", e)

        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal server error",
            },
        )