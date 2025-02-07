Public API for HNG Internship Stage 0

This is a simple FastAPI-based public API developed as part of the (HNG Internship Stage 0) task. The API returns basic information including the developer's registered email, the current date and time in ISO 8601 format (UTC), and the GitHub repository URL.

Features
- Returns email, timestamp, and GitHub repo URL in JSON format.
- Ensures 'current_datetime' is dynamically generated in ISO 8601 format (UTC).
- Handles Cross-Origin Resource Sharing (CORS).
- Provides a publicly accessible endpoint for easy access.

Technology Stack
- Programming Language: Python
- Framework: FastAPI
- Web Server: Uvicorn

API Endpoint
GET /
Response Format (200 OK)
json
{
  "email": "kazeemj565@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/kazeemj565/hng_task0"
}

Deployment
The API was deployed to a publicly accessible endpoint.The platform used  is Render.
The URL is: https://hng-task0-1-1sg3.onrender.com
