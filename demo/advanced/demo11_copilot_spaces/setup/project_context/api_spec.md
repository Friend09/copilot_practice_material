# API Specification

## v1 Endpoints (Current)

All v1 endpoints require a valid session cookie for authentication.

### User Service

| Method | Endpoint              | Description                |
|--------|-----------------------|----------------------------|
| POST   | `/api/v1/auth/login`  | Login with email/password  |
| POST   | `/api/v1/auth/logout` | Invalidate session         |
| GET    | `/api/v1/users/me`    | Get current user profile   |
| PUT    | `/api/v1/users/me`    | Update current user profile|

### Product Service

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/v1/products`        | List products (paginated)|
| GET    | `/api/v1/products/:id`    | Get product by ID        |
| POST   | `/api/v1/products`        | Create product (admin)   |
| PUT    | `/api/v1/products/:id`    | Update product (admin)   |

### Order Service

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| POST   | `/api/v1/orders`          | Create order             |
| GET    | `/api/v1/orders`          | List user orders         |
| GET    | `/api/v1/orders/:id`      | Get order by ID          |

## v2 Endpoints (Planned)

All v2 endpoints require a valid JWT token in the `Authorization: Bearer <token>` header.

### User Service

| Method | Endpoint                  | Description                    |
|--------|---------------------------|--------------------------------|
| POST   | `/api/v2/auth/token`      | Obtain JWT token (login)       |
| POST   | `/api/v2/auth/refresh`    | Refresh expired JWT token      |
| POST   | `/api/v2/auth/revoke`     | Revoke refresh token (logout)  |
| GET    | `/api/v2/users/me`        | Get current user profile       |
| PATCH  | `/api/v2/users/me`        | Partial update user profile    |

### Product Service

| Method | Endpoint                          | Description                  |
|--------|-----------------------------------|------------------------------|
| GET    | `/api/v2/products`                | List products (cursor-based) |
| GET    | `/api/v2/products/:id`            | Get product by ID            |
| POST   | `/api/v2/products`                | Create product (admin)       |
| PATCH  | `/api/v2/products/:id`            | Partial update product       |
| GET    | `/api/v2/products/search`         | Full-text product search     |

### Order Service

| Method | Endpoint                          | Description                  |
|--------|-----------------------------------|------------------------------|
| POST   | `/api/v2/orders`                  | Create order                 |
| GET    | `/api/v2/orders`                  | List user orders (filtered)  |
| GET    | `/api/v2/orders/:id`              | Get order by ID              |
| PATCH  | `/api/v2/orders/:id/cancel`       | Cancel a pending order       |

## Breaking Changes (v1 to v2)

1. **Authentication**: Session cookies replaced by JWT Bearer tokens
2. **Pagination**: Offset-based pagination replaced by cursor-based pagination
3. **Updates**: `PUT` (full replace) replaced by `PATCH` (partial update)
4. **Login endpoint**: `/auth/login` renamed to `/auth/token` (returns JWT)
5. **Logout endpoint**: `/auth/logout` renamed to `/auth/revoke` (revokes refresh token)
6. **Response envelope**: v2 wraps all responses in `{ "data": ..., "meta": ... }`

## Migration Path

1. Run v1 and v2 endpoints in parallel during the migration period
2. API gateway routes by version prefix (`/api/v1/` vs `/api/v2/`)
3. v1 endpoints remain active for 6 months after v2 launch
4. Clients migrate at their own pace; deprecation headers added to v1 responses
5. Monitor v1 traffic and notify remaining clients before final shutdown
