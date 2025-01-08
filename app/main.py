from fastapi import FastAPI
from app.api import router
from app.container import Container
from app.middleware.auth_middleware import auth_middleware

container = Container()

db = container.db()
db.create_database()

# Creación de la aplicación FastAPI
app = FastAPI(
    title="Potato prediction",
    description="API para la predicción de la características ideales de papa.",
    version="0.1"
)

# Add auth middleware
app.middleware("http")(auth_middleware)

# Inyección de dependencias
app.container = container

# Inclusión de las rutas en la aplicación
app.include_router(router)