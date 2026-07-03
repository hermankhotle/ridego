from fastapi import FastAPI
import redis
import os
import json
import threading

app = FastAPI(title="Report Service")
r = redis.Redis(host=os.getenv("REDIS_URL", "redis"), port=6379, decode_responses=True)

def listen_to_gps():
    pubsub = r.pubsub()
    pubsub.subscribe('gps-updates')
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            print(f"Sending Push Notification: Driver {data['driver_id']} moved to {data['lat']}, {data['lng']}")
            # In real app, send FCM/HMS push here.

# Start listener in background thread
threading.Thread(target=listen_to_gps, daemon=True).start()

@app.get("/health")
async def health():
    return {"status": "report-service healthy"}
