from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.paypal import router as paypal_router
from app.api.v1.agents import router as agents_router

app = FastAPI(
    title="NexusFlow AI: Autonomous B2B Multi-Agent Treasury & Invoicing Engine",
    description="Award-winning Agentic Commerce backend built for the PayPal AI Hackathon.",
    version="1.0.0"
)

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(paypal_router, prefix="/api/v1")
app.include_router(agents_router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
def root_health_check():
    """Verifies that the NexusFlow AI backend service is online and operational."""
    return {
        "status": "online",
        "service": "NexusFlow AI Treasury Engine",
        "hackathon": "PayPal AI Hackathon 2026",
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.main("main:app", host="0.0.0.0", port=8000, reload=True)
