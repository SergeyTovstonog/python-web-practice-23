from fastapi import HTTPException


def exception_handler(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    return wrapper
