from fastapi import FastAPI
import redis
import os
from pydantic import BaseModel

app = FastAPI(title="Trip Service")
r = redis.Redis(host=os.getenv("REDIS_URL", "redis"), port=6379, decode_responses=True)

class TripRequest(BaseModel):
    driver_id: int
    pickup: str
    dropoff: str

@app.get("/health")
async def health():
    return {"status": "trip-service healthy"}

@app.post("/trips")
async def create_trip(trip: TripRequest):
    trip_id = 101 # Mock ID
    # Cache trip in Redis for fast access
    r.setex(f"trip:{trip_id}:driver", 3600, trip.driver_id)
    return {"trip_id": trip_id, "status": "created", "driver": trip.driver_id}
