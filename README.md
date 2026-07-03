# RideGo Platform

A comprehensive microservices-based ride-sharing platform built with Python FastAPI, PostgreSQL, Redis, and RabbitMQ.

## 🏗️ Architecture

The platform consists of:

### Core Services (Ports 8001-8007)
- **Auth Service (8001)**: User registration, JWT generation, role-based access control
- **User Service (8002)**: Staff/driver profiles and assignments
- **Trip Service (8003)**: Trip creation, scheduling, route optimization
- **Tracking Service (8004)**: Live GPS ingestion, geofencing, ETA calculation
- **Notification Service (8005)**: FCM/HMS push notifications, email, SMS
- **Finance Service (8006)**: Payments, invoices, payroll integration
- **Report Service (8007)**: Analytics, PDF generation, data exports

### Infrastructure
- **API Gateway (8000)**: Nginx reverse proxy for routing and load balancing
- **PostgreSQL**: Primary relational database
- **Redis**: Caching and session storage
- **RabbitMQ**: Asynchronous message queue

### Clients
- **Mobile App**: Flutter-based customer and driver applications
- **Web Dashboard**: React/Next.js admin and company dashboards

### Shared Libraries
- Python SDK with common models, utilities, and business logic

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+ (for web dashboard)
- Flutter SDK (for mobile app)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/hermankhotle/ridego.git
   cd ridego
   ```

2. **Copy environment file**
   ```bash
   cp infrastructure/.env.example .env
   ```

3. **Start infrastructure**
   ```bash
   cd infrastructure
   docker-compose up -d
   ```

4. **Verify services are running**
   ```bash
   curl http://localhost:8000/health
   ```

5. **Access services**
   - API Gateway: http://localhost:8000
   - Auth Service: http://localhost:8001
   - User Service: http://localhost:8002
   - Trip Service: http://localhost:8003
   - Tracking Service: http://localhost:8004
   - Notification Service: http://localhost:8005
   - Finance Service: http://localhost:8006
   - Report Service: http://localhost:8007
   - RabbitMQ Management: http://localhost:15672 (guest/guest)

## 📁 Directory Structure

```
ridego/
├── api-gateway/              # Kong / Nginx (Entry Point)
├── services/
│   ├── auth-service/         # User auth & JWT (Port 8001)
│   ├── user-service/         # User profiles (Port 8002)
│   ├── trip-service/         # Trip management (Port 8003)
│   ├── tracking-service/     # GPS & Geofencing (Port 8004)
│   ├── notification-service/ # Push/Email/SMS (Port 8005)
│   ├── finance-service/      # Payments & Invoices (Port 8006)
│   └── report-service/       # Analytics & Exports (Port 8007)
├── shared-libraries/         # Python SDK
├── mobile-app/               # Flutter client
├── web-dashboard/            # React/Next.js dashboard
├── infrastructure/           # Terraform & Docker Compose
└── README.md
```

## 🔧 Configuration

Environment variables are defined in `.env`. Key configurations:

- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `RABBITMQ_URL`: RabbitMQ connection string
- `JWT_SECRET`: Secret key for JWT signing
- `STRIPE_SECRET_KEY`: Stripe API key
- `FIREBASE_PROJECT_ID`: Firebase project ID

See `infrastructure/.env.example` for all available options.

## 📚 API Documentation

Each service provides Swagger/OpenAPI documentation:

- Auth Service: http://localhost:8001/docs
- User Service: http://localhost:8002/docs
- Trip Service: http://localhost:8003/docs
- Tracking Service: http://localhost:8004/docs
- Notification Service: http://localhost:8005/docs
- Finance Service: http://localhost:8006/docs
- Report Service: http://localhost:8007/docs

## 🐛 Troubleshooting

### Services not starting
```bash
# Check logs
docker-compose logs <service-name>

# Rebuild containers
docker-compose down
docker-compose up -d --build
```

### Database connection issues
```bash
# Check PostgreSQL is healthy
docker-compose exec postgres pg_isready -U ridego

# Run migrations
docker-compose exec auth-service alembic upgrade head
```

### Redis connection issues
```bash
# Check Redis is running
docker-compose exec redis redis-cli ping
```

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 📞 Support

For issues and questions, please open a GitHub issue.
