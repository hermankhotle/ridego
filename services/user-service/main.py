from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="User Service")

class UserProfile(BaseModel):
    id: int
    name: str
    role: str

@app.get("/health")
async def health():
    return {"status": "user-service healthy"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Mock Data
    return UserProfile(id=user_id, name="John Doe", role="Driver")

@app.post("/users")
async def create_user(user: UserProfile):
    return {"message": f"User {user.name} created successfully"}
