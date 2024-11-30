from fastapi import FastAPI
from app.routes.studentRoutes import router as student_router

app = FastAPI()

app.include_router(student_router)

@app.get("/")
def read_root():
    return {"message": "Cosmocloud Assignment is running"}
