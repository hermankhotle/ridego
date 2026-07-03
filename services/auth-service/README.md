# Auth Service

Handles user registration, JWT token generation, and role-based access control.

## Configuration
- Port: 8001
- Database: PostgreSQL
- Key Endpoints:
  - POST /auth/register
  - POST /auth/login
  - POST /auth/refresh
  - POST /auth/logout
