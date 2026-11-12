# ⚡ NexusFlow AI: Autonomous B2B Treasury & Invoicing Engine

> **PayPal AI Hackathon Submission (November 2026)**  
> Autonomous multi-agent B2B treasury management, intelligent compliance auditing, and instant global disbursement powered by FastAPI, Streamlit, and the PayPal Developer Platform.

---

## 🌟 Overview

Cross-border B2B transactions are traditionally bogged down by high transaction fees, manual wire delays, and complex compliance review bottlenecks. **NexusFlow AI** solves this by putting AI agents in the driver's seat of corporate liquidity. 

When a vendor submits an invoice, our multi-agent swarm instantly evaluates risk vectors, performs NLP compliance checks on line items, and autonomously orchestrates secure escrow creation (PayPal v2 Orders) and instant disbursements (PayPal v1 Payouts).

---

## 🧠 Multi-Agent Swarm Architecture

1. **Risk & Anomaly Assessment Agent:** Analyzes transaction velocity, payout threshold limits, and entity reputation scores.
2. **Regulatory Compliance Agent:** Parses invoice descriptions and line-item details using NLP logic to flag invalid identifiers or policy violations.
3. **PayPal Execution Agent:** Automatically authenticates via OAuth2 and securely executes instant vendor disbursements.
4. **Disputes & Appeals Queue:** Provides administrators with a manual review workspace to audit flagged transactions and force-override edge cases with a full cryptographic audit log.

---


[![Streamlit App](https://static.shields.io/badge/Streamlit-Live%20App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://nexusflow-ai-6wtdgjyd5qoxff9k7mcax8.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PayPal Hackathon](https://img.shields.io/badge/PayPal-AI%20Hackathon-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://developer.paypal.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)



## 🛠️ Technology Stack

* **Backend:** Python, FastAPI, Uvicorn, Pydantic, Requests
* **Frontend GUI:** Streamlit (Dark Fintech Glassmorphic Dashboard)
* **Payment Integration:** PayPal REST APIs (v2 Checkout Orders & v1 Payouts Sandbox)
* **Automation & Logging:** Session-persistent audit ledgers with automated CSV compliance reporting

---

## 🚀 Local Installation & Setup Instructions

Follow these instructions to run the application locally for evaluation.

### Prerequisites
* Python 3.10+ installed on your system
* Git / Git Bash

### Step 1: Clone the Repository & Setup Backend
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/nexusflow-ai.git](https://github.com/YOUR_GITHUB_USERNAME/nexusflow-ai.git)
cd nexusflow-ai/backend

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # On Linux/Mac use: source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn requests pydantic

# Run the FastAPI server
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
he backend API will be live at http://127.0.0.1:8000 (Interactive docs at /docs).

Step 2: Run the Streamlit Frontend GUI
Open a second terminal window, then navigate to the frontend directory:

Bash
cd nexusflow-ai/frontend

# Install frontend dependencies
pip install streamlit requests pandas plotly

# Launch the Streamlit dashboard
streamlit run app.py
The interactive command center will open automatically in your browser at http://localhost:8501.

💡 How to Use the Dashboard
Executive Treasury Overview: Monitor real-time system uptime, processed liquidity volume, and fraud mitigation statistics.

Multi-Agent Swarm Execution: Use the quick-load demo scenarios to test standard approved payouts, high-amount anomalies ($15,000 threshold blocks), or compliance violations.

Disputes & Appeals Queue: Review flagged transactions and test the administrator override feature.

PayPal Direct Sandbox Gateway: Directly test raw v2 Checkout Orders and v1 Payout requests.

Audit Ledger: Inspect the immutable transaction log and export compliance reports as a CSV.

📜 License
This project is open-source and licensed under the MIT License.
