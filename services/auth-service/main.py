from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import os
from datetime import datetime, timedelta

app = FastAPI(title="Auth Service")
SECRET_KEY = os.getenv("JWT_SECRET", "default_secret")
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/health")
async def health():
    return {"status": "auth-service healthy"}

@app.post("/auth/login")
async def login(request: LoginRequest):
    # Mock DB check - Replace with actual PostgreSQL check later
    if request.username == "admin" and request.password == "password":
        token = jwt.encode({
            "sub": request.username,
            "role": "admin",
            "exp": datetime.utcnow() + timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
