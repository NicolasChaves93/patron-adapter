from fastapi import FastAPI
import uvicorn
from app.routes.convert import router

app = FastAPI()

# Registrar las rutas
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
