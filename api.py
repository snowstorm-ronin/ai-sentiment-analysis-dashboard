from fastapi import FastAPI
from pydantic import BaseModel
from model import analyze_sentiment
from database import init_db, save_feedback

# Create the FastAPI app - THIS MUST BE AT TOP LEVEL
app = FastAPI(title="Customer Sentiment API")

# This runs when the API starts
@app.on_event("startup")
async def startup():
    """Initialize the database when API starts"""
    init_db()
    print("API is ready to analyze sentiment!")

# Define the request format
class FeedbackRequest(BaseModel):
    text: str

# Define the response format
class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: FeedbackRequest):
    """Main endpoint for sentiment analysis"""
    # Analyze sentiment
    result = analyze_sentiment(request.text)
    
    # Save to database
    save_feedback(request.text, result["label"], result["confidence"])
    
    # Return result
    return SentimentResponse(
        text=request.text,
        sentiment=result["label"],
        confidence=result["confidence"]
    )

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running! Use /predict endpoint."}