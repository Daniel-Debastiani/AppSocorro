from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from .routes.user_routes import router as user_router
from .routes.emergencia_routes import router as emergencia_router
from .routes.verifica_documento_routes import router as verifica_documento_router


app = FastAPI()

app.include_router(user_router, tags=["User"])
app.include_router(emergencia_router, tags=["Emergência"])
app.include_router(verifica_documento_router, tags=["Verificação de Documento"])

app.mount("/static", StaticFiles(directory="/home/daniel-debastiani/Documents/PROJECTS/AppSocorro/processed_images"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
