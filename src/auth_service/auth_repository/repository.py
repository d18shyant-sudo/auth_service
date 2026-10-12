from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth_service.auth_model.model import Account
from auth_service.utils.password import hash_password,verify_password
class AuthRepository:

    @staticmethod
    async def store_account_detail(
        db: AsyncSession,
        user_data
    ):
        new_account = Account(
            username=user_data.username,
            password=hash_password(user_data.password),
            email=user_data.emailid,
        )

        db.add(new_account)

        await db.commit()

        return new_account

    @staticmethod
    async def verify_user(
        db: AsyncSession,
        user_data,
    ) -> bool:

        result = await db.execute(
            select(Account).where(
                Account.email == user_data.emailid
            )
        )

        account = result.scalar_one_or_none()

        if account is None:
            return False

        return verify_password(
            password=user_data.password,
            hashed_password=account.password,
        )
    @staticmethod
    async def get_user_id(
        db: AsyncSession,
        user_data,
    ) -> bool:

        result = await db.execute(
            select(Account).where(
                Account.email == user_data.emailid
            )
        )

        account = result.scalar_one_or_none()
        
        return account.id