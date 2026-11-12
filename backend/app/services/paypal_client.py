import os
import requests
from requests.auth import HTTPBasicAuth

class PayPalClient:
    """
    Core PayPal REST API Client configured for Sandbox environment.
    Handles OAuth2 authentication, Orders (Checkout), and Payouts (Disbursements).
    """
    def __init__(self, client_id: str = None, client_secret: str = None, mode: str = "sandbox"):
        self.client_id = client_id or os.getenv("PAYPAL_CLIENT_ID", "")
        self.client_secret = client_secret or os.getenv("PAYPAL_CLIENT_SECRET", "")
        self.mode = mode
        self.base_url = (
            "https://api-m.sandbox.paypal.com"
            if mode == "sandbox"
            else "https://api-m.paypal.com"
        )
        self._access_token = None

    def get_access_token(self) -> str:
        """Authenticates with PayPal and retrieves a Bearer access token."""
        url = f"{self.base_url}/v1/oauth2/token"
        headers = {"Accept": "application/json", "Accept-Language": "en_US"}
        data = {"grant_type": "client_credentials"}
        
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=HTTPBasicAuth(self.client_id, self.client_secret)
        )
        
        if response.status_code == 200:
            self._access_token = response.json().get("access_token")
            return self._access_token
        else:
            raise Exception(f"Failed to obtain PayPal Access Token: {response.status_code} - {response.text}")

    def create_order(self, amount: str, currency: str = "USD", return_url: str = "https://example.com/return", cancel_url: str = "https://example.com/cancel") -> dict:
        """Creates a PayPal Checkout Order for secure deposits/payments."""
        token = self.get_access_token()
        url = f"{self.base_url}/v2/checkout/orders"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": currency,
                        "value": amount
                    }
                }
            ],
            "application_context": {
                "return_url": return_url,
                "cancel_url": cancel_url
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(f"Failed to create PayPal order: {response.status_code} - {response.text}")

    def create_payout(self, recipient_email: str, amount: str, currency: str = "USD", note: str = "NexusFlow AI Autonomous Treasury Payout") -> dict:
        """Executes an automated vendor or freelancer payout via PayPal Payouts API."""
        token = self.get_access_token()
        url = f"{self.base_url}/v1/payments/payouts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "sender_batch_header": {
                "sender_batch_id": f"batch_{os.urandom(4).hex()}",
                "email_subject": "Automated Payout from NexusFlow AI",
                "email_message": "Your multi-agent treasury payout has been successfully settled."
            },
            "items": [
                {
                    "recipient_type": "EMAIL",
                    "amount": {
                        "value": amount,
                        "currency": currency
                    },
                    "note": note,
                    "receiver": recipient_email,
                    "sender_item_id": f"item_{os.urandom(4).hex()}"
                }
            ]
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(f"Failed to execute PayPal payout: {response.status_code} - {response.text}")
