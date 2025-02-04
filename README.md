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
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

Setup Instructions
1. Clone the Repository
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install Dependencies**
```sh
pip install -r requirements.txt
```
4. Run the API Locally**
```sh
uvicorn fastapi_public_api:app --reload
```

Deployment
The API was deployed to a publicly accessible endpoint.The platform used  is Render.

Links
- [HNG Internship](https://hng.tech/)
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire Other Developers](https://hng.tech/hire/)

