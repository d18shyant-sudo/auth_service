from src.auth_service.config.database import sessionlocal
async def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        await db.close()