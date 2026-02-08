# System Architecture

## Overview

Our e-commerce platform uses a microservices architecture with four core services
communicating through an API gateway and an event-driven message bus.

## Services

### 1. User Service

- Manages user accounts, profiles, and authentication
- Database: PostgreSQL (dedicated instance)
- Current auth: session cookies stored in Redis
- Planned auth: JWT tokens issued by this service, validated at the gateway

### 2. Product Service

- Manages product catalog, categories, and inventory
- Database: PostgreSQL (dedicated instance)
- Exposes search and filtering endpoints
- Publishes inventory change events to the message bus

### 3. Order Service

- Handles order creation, status tracking, and fulfillment
- Database: PostgreSQL (dedicated instance)
- Subscribes to inventory events for stock validation
- Publishes order status events (created, shipped, delivered)

### 4. Payment Service

- Processes payments and manages billing records
- Database: PostgreSQL (dedicated instance)
- Integrates with Stripe for payment processing
- Subscribes to order events to trigger payment flows

## API Gateway

- **Technology**: Kong API Gateway
- **Responsibilities**: routing, rate limiting, authentication enforcement, request logging
- Currently validates session cookies by calling the User Service
- v2 plan: validate JWT tokens locally at the gateway (no User Service call needed)

## Communication Patterns

- **Synchronous**: REST API calls through the gateway for client-facing requests
- **Asynchronous**: RabbitMQ message bus for inter-service events
- **Event types**: inventory changes, order status updates, payment confirmations

## Current Authentication (v1)

- Session cookies issued on login by the User Service
- Cookies stored in Redis with a 24-hour TTL
- Gateway forwards cookies to User Service for validation on every request
- Drawback: User Service is a bottleneck for all authenticated requests

## Planned Authentication (v2)

- JWT tokens issued on login by the User Service
- Tokens signed with RS256 (asymmetric keys)
- Gateway validates tokens locally using the public key (no User Service call)
- Token TTL: 1 hour with refresh token rotation
- Advantage: eliminates the User Service bottleneck for auth validation
