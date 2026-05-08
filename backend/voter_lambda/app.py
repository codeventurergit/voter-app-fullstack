import asyncio
import random
from fastapi import FastAPI # Missing Import
import httpx # Required if you plan to use the Ollama block

# 1. Define the app variable that Render is looking for
app = FastAPI()

# Allow cross origin access:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# 2. Add a basic root route so Render's health check passes immediately
@app.get("/")
async def root():
    return {"status": "ok", "message": "Voter Strategy API is live"}

# 3. Your specific endpoint
@app.post("/voters/{voter_id}/ai-strategy")
async def get_ai_strategy(voter_id: str):
    """
    AI Strategy Endpoint
    """
    # Simulated processing time to mirror LLM latency
    await asyncio.sleep(1.2) 
    
    mock_responses = [
        "Focus on community-driven infrastructure and job training programs.",
        "Highlight environmental sustainability and green energy incentives.",
        "Emphasize accessible healthcare and youth mentorship initiatives."
    ]
    
    return {
        "voter_id": voter_id,
        "strategy": f"[DEMO MODE] {random.choice(mock_responses)}"
    }
