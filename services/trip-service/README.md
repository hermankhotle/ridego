# Trip Service

Handles trip creation, scheduling, and route optimization.

## Configuration
- Port: 8003
- Database: PostgreSQL
- Cache: Redis
- Key Endpoints:
  - POST /trips
  - GET /trips/{trip_id}
  - PUT /trips/{trip_id}
  - POST /trips/{trip_id}/optimize-route
  - GET /trips/status
