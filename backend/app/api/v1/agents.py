from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from app.agents.orchestrator import NexusFlowOrchestrator

router = APIRouter(prefix="/agents", tags=["Multi-Agent Orchestration"])
orchestrator = NexusFlowOrchestrator()

class AgentExecutionRequest(BaseModel):
    vendor_email: str = Field(..., example="vendor@example.com", description="Recipient vendor/freelancer PayPal email")
    amount: str = Field(..., example="2500.00", description="Invoice payment amount")
    invoice_text: str = Field(..., example="Invoice #1094 for Q3 AI Infrastructure Development & Cloud Migration.", description="Invoice content for NLP and compliance parsing")

@router.post("/execute-treasury", summary="Run Multi-Agent Treasury & PayPal Settlement Workflow")
def execute_treasury_workflow(payload: AgentExecutionRequest):
    """
    Triggers the autonomous agent swarm:
    1. Risk Agent evaluates anomaly and fraud metrics.
    2. Compliance Agent parses contract rules.
    3. PayPal Payouts API executes secure settlement if approved.
    """
    try:
        result = orchestrator.process_invoice_and_execute(
            vendor_email=payload.vendor_email,
            amount=payload.amount,
            invoice_text=payload.invoice_text
        )
        return {
            "status": "success",
            "orchestration_result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
