from fastapi import FastAPI
from datetime import datetime
from pytz import timezone 

app = FastAPI() 

@app.get("/")
def get_info():
    return {
        "email": "Agimuche1@gmail.com", 
        "current_datetime": datetime.now(timezone("UTC")).isoformat(),
        "github_url": "https:// github.com/agimuche/hng12-backend-task"
    }