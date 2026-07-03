# Tracking Service

Ingests live GPS data, handles geofencing, and calculates ETA.

## Configuration
- Port: 8004
- Database: PostgreSQL
- Cache: Redis
- Message Queue: RabbitMQ/Kafka
- Key Endpoints:
  - POST /tracking/gps
  - GET /tracking/location/{driver_id}
  - POST /tracking/geofence
  - GET /tracking/eta/{trip_id}
