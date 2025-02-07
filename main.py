from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import uvicorn


# Create the FastAPI app instance
app = FastAPI(
    title="HNG12 Public API",
    description="An API that returns registered email, current datetime, and GitHub URL.",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace with your actual registered email and GitHub URL
REGISTERED_EMAIL = "kazeemj565@gmail.com"
GITHUB_URL = "https://github.com/kazeemj565/hng_task0"

@app.get("/", status_code=200)
async def get_request():
    
    try:
        response = {
            "email": REGISTERED_EMAIL,
            "current_datetime": datetime.now(timezone.utc).isoformat(),
            "github_url": GITHUB_URL
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
