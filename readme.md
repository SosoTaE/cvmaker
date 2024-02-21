# CvMaker Server API Documentation

## General Information

- **Base URL**: The base URL for all endpoints is `http://<server-ip>:8000`. Replace `<server-ip>` with the actual IP address of the server.
- **Content-Type**: All requests must be sent with the `Content-Type: application/json` header unless otherwise specified.
- **Authorization**: Protected routes require an access token in the `Authorization` header in the format `<access_token>`.

## Middleware

### Access Token Verification

- **Description**: Automatically verifies the access token for protected routes.
- **Affected Routes**: All routes except `/login`, `/registration`, and `/refresh`.

## Endpoints

### Registration

- **URL**: `/registration`
- **Method**: `POST`
- **Authorization**: Not required
- **Description**: Registers a new user.
- **Request Body**:
  ```json
  {
    "password": "string",
    "email": "string"
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**: `{ "message": "User registered successfully." }`
- **Error Response**:
  - **Code**: 400
  - **Content**: `{ "message": "User registration failed." }`

### Login

- **URL**: `/login`
- **Method**: `POST`
- **Authorization**: Not required
- **Description**: Authenticates a user and returns an access token.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**: `{ "access_token": "string", "refresh_token": "string" }`
- **Error Response**:
  - **Code**: 401
  - **Content**: `{ "message": "Invalid credentials." }`

### Refresh

- **URL**: `/refresh`
- **Method**: `POST`
- **Authorization**: Required (Refresh Token)
- **Description**: Refreshes an expired access token using a refresh token.
- **Request Body**: None
- **Success Response**:
  - **Code**: 200
  - **Content**: `{ "accessToken": "new_access_token", "refreshToken": new_refresh_token }`
- **Error Response**:
  - **Code**: 401
  - **Content**: `{ "message": "Invalid or expired refresh token." }`

## Notes

- Replace `string` in the sample request bodies with actual values.
- The access token must be included in the `Authorization` header for routes requiring authorization.
- Ensure to handle errors gracefully in the frontend application by checking the status code and error messages returned by the API.

---