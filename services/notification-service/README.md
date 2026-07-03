# Notification Service

Handles push notifications via FCM/HMS, email, and SMS.

## Configuration
- Port: 8005
- Message Queue: RabbitMQ/Kafka
- Providers:
  - Firebase Cloud Messaging (FCM)
  - Huawei Mobile Services (HMS)
  - Email (SMTP)
  - SMS (Twilio/AWS SNS)
- Key Endpoints:
  - POST /notifications/send
  - POST /notifications/batch
  - GET /notifications/history
