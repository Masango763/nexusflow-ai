from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from app.services.paypal_client import PayPalClient

router = APIRouter(prefix="/paypal", tags=["PayPal Treasury & Payments"])
paypal_client = PayPalClient()

class OrderRequest(BaseModel):
    amount: str = Field(..., example="150.00", description="Total transaction amount")
    currency: str = Field(default="USD", example="USD", description="Currency code")
    return_url: str = Field(default="https://example.com/return", description="Approval return URL")
    cancel_url: str = Field(default="https://example.com/cancel", description="Cancellation URL")

class PayoutRequest(BaseModel):
    recipient_email: str = Field(..., example="freelancer@example.com", description="Recipient PayPal email")
    amount: str = Field(..., example="150.00", description="Payout amount")
    currency: str = Field(default="USD", example="USD", description="Currency code")
    note: str = Field(default="NexusFlow AI Automated Payout", description="Note accompanying payment")

@router.post("/order", summary="Create PayPal Checkout Order")
def create_paypal_order(payload: OrderRequest):
    """
    Initiates an escrow or checkout order via PayPal Sandbox API v2.
    Returns approval links for client authorization.
    """
    try:
        order = paypal_client.create_order(
            amount=payload.amount,
            currency=payload.currency,
            return_url=payload.return_url,
            cancel_url=payload.cancel_url
        )
        return {
            "status": "success",
            "order_id": order.get("id"),
            "status_details": order.get("status"),
            "links": order.get("links", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/payout", summary="Execute Autonomous Vendor/Freelancer Payout")
def execute_paypal_payout(payload: PayoutRequest):
    """
    Triggers an instant automated disbursement to a recipient's PayPal account 
    via PayPal Payouts API based on multi-agent validation.
    """
    try:
        payout = paypal_client.create_payout(
            recipient_email=payload.recipient_email,
            amount=payload.amount,
            currency=payload.currency,
            note=payload.note
        )
        batch_header = payout.get("batch_header", {})
        return {
            "status": "success",
            "batch_id": batch_header.get("payout_batch_id"),
            "batch_status": batch_header.get("batch_status"),
            "raw_response": payout
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
