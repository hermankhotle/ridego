from fastapi import FastAPI
import redis
import os
import json

app = FastAPI(title="Tracking Service")
r = redis.Redis(host=os.getenv("REDIS_URL", "redis"), port=6379, decode_responses=True)

@app.get("/health")
async def health():
    return {"status": "tracking-service healthy"}

@app.post("/tracking/gps")
async def update_gps(driver_id: int, lat: float, lng: float):
    # Update live location in Redis
    r.setex(f"driver:{driver_id}:location", 60, json.dumps({"lat": lat, "lng": lng}))
    
    # Publish to Notification Service (via Redis Pub/Sub)
    r.publish("gps-updates", json.dumps({
        "driver_id": driver_id, 
        "lat": lat, 
        "lng": lng
    }))
    return {"status": "location updated"}
