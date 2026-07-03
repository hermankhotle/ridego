# Report Service

Handles analytics, PDF generation, and data exports.

## Configuration
- Port: 8007
- Database: PostgreSQL
- Cache: Redis
- File Storage: S3/MinIO
- Key Endpoints:
  - GET /reports/trips
  - GET /reports/revenue
  - GET /reports/drivers
  - POST /reports/export
  - GET /reports/{report_id}/download
