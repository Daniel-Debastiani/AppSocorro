from fastapi import FastAPI
from .routes.user_routes import router as user_router
from .routes.emergencia_routes import router as emergenci_router

app = FastAPI()

app.include_router(user_router)
app.include_router(emergenci_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
