from auth_service.auth_repository.repository import AuthRepository
from auth_service.utils.generate_token import create_access_token
import logging
logging.basicConfig(level=logging.INFO)
from sqlalchemy.ext.asyncio import AsyncSession
class AuthService:
    async def store_account(db:AsyncSession,userdata):
        result = await AuthRepository.store_account_detail(db=db,user_data=userdata)
        return result
    async def verify_user(db:AsyncSession,userdata):
        result = await AuthRepository.verify_user(db=db,user_data=userdata)
        if result:
            user_id = await AuthRepository.get_user_id(db=db,user_data=userdata)
            token = create_access_token(user_id=user_id)
            return token
        return result