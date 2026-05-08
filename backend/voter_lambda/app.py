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

# 3. Endpoint for a specific voter insight
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

# 4. Endpont for all voter insights
@app.get("/voters")
async def list_voters(limit: int = 100):
    """Retrieves a list of voters from DynamoDB to populate the dashboard."""
    try:
        table = dynamodb.Table('VoterTable')
        response = table.scan(Limit=limit)
        return {"count": len(response['Items']), "voters": response['Items']}
    except Exception as e:
        return {"error": str(e)}

@app.post("/dev/seed")
async def seed_voters():
    """Seeds the database with sample data for demo purposes."""
    table = dynamodb.Table('VoterTable')
    sample_cities = ["Arlington", "Alexandria", "Richmond", "Roanoke"]
    
    for i in range(50):
        voter_id = f"V-{1000 + i}"
        table.put_item(Item={
            'voter_id': voter_id,
            'name': f"Sample Voter {i}",
            'city': random.choice(sample_cities),
            'interest': random.choice(["Education", "Healthcare", "Economy", "Climate"])
        })
    return {"status": "success", "message": "50 records seeded."}
