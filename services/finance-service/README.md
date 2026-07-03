# Finance Service

Handles payments, invoices, and payroll integration.

## Configuration
- Port: 8006
- Database: PostgreSQL
- Payment Providers:
  - Stripe
  - PayPal
  - Local Payment Gateways
- Key Endpoints:
  - POST /payments
  - GET /payments/{payment_id}
  - POST /invoices
  - GET /invoices
  - POST /payroll/process
