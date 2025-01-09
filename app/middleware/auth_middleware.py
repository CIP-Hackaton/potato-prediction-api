from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from jwt.exceptions import InvalidTokenError
from typing import Callable
import jwt

from app.services.jwt_service import TokenServiceJWT
from app.config import settings

async def auth_middleware(request: Request, call_next: Callable):

    # Permitir solicitudes OPTIONS sin autenticación
    if request.method == "OPTIONS":
        return await call_next(request)


    # Skip auth routes and documentation
    if  request.url.path.startswith("/api/v1/auth/") or \
        request.url.path.startswith("/docs") or \
        request.url.path.startswith("/openapi.json") or \
        request.url.path.startswith("/redoc") or \
        request.url.path.startswith("/health"):
        return await call_next(request)

    # Get authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Missing or invalid authorization header"}
        )

    # Extract token
    token = auth_header.split(" ")[1]
    
    try:
        # Verify token
        jwt_service = TokenServiceJWT(secret_key=settings.JWT_SECRET_KEY)
        payload = jwt_service.verify_token(token)
        
        # Store user_id in request state
        request.state.user_id = payload.get("user_id")
        
        return await call_next(request)
        
    except InvalidTokenError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid token"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)}
        )
