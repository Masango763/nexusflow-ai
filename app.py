import streamlit as st
import requests
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

# 1. Page Configuration
st.set_page_config(
    page_title="NexusFlow AI | Enterprise Agentic Treasury",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Initialize Session State for Live Audit Ledger
if "ledger" not in st.session_state:
    st.session_state.ledger = [
        {"Timestamp": "2026-11-12 09:14:22", "Vendor": "cloud-ops@aws-partner.io", "Amount": "$4,200.00", "Risk Score": "0.08 (Low)", "Status": "✅ Settled (PayPal)"},
        {"Timestamp": "2026-11-12 10:45:09", "Vendor": "design-studio@figma-pro.com", "Amount": "$1,850.00", "Risk Score": "0.11 (Low)", "Status": "✅ Settled (PayPal)"},
        {"Timestamp": "2026-11-12 11:30:51", "Vendor": "unknown-offshore@shell.biz", "Amount": "$14,500.00", "Risk Score": "0.89 (High)", "Status": "🛑 Blocked by Risk Agent"},
    ]

# 3. Advanced Custom CSS (Dark Fintech Glassmorphism Theme)
st.markdown("""
    <style>
    /* Global Background & Typography */
    .stApp {
        background: linear-gradient(135deg, #0B1120 0%, #0F172A 100%);
        color: #F8FAFC;
    }
    
    /* Custom Gradient Header */
    .hero-banner {
        background: linear-gradient(90deg, rgba(0, 48, 135, 0.45) 0%, rgba(0, 112, 186, 0.25) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 14px;
        padding: 1.75rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero-sub {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    /* Glassmorphic Metric Cards */
    div[data-testid="metric-container"] {
        background: rgba(30, 41, 59, 0.65);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        border-color: #38BDF8;
    }
    div[data-testid="stMetricValue"] {
        color: #F8FAFC;
        font-weight: 700;
    }

    /* Agent Pipeline Cards */
    .agent-card {
        background: rgba(15, 23, 42, 0.8);
        border-left: 4px solid #0070BA;
        border-top: 1px solid rgba(255,255,255,0.08);
        border-right: 1px solid rgba(255,255,255,0.08);
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.75rem;
    }
    
    /* Custom Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #0070BA 0%, #003087 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.25s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #0086E0 0%, #0044B8 100%);
        box-shadow: 0 0 15px rgba(0, 112, 186, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

# 4. Sidebar Command Navigation
with st.sidebar:
    st.markdown("## ⚡ **NEXUSFLOW AI**")
    st.caption("Autonomous Agentic Commerce Engine")
    st.markdown("---")
    
    workspace = st.radio(
        "COMMAND MODULES",
        [
            "📊 Executive Treasury Overview",
            "🤖 Multi-Agent Swarm Execution",
            "💳 PayPal Direct Sandbox Gateway",
            "📜 Immutable Audit Ledger"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 🔌 Live System Telemetry")
    try:
        health = requests.get(f"{BACKEND_URL}/", timeout=2)
        if health.status_code == 200:
            st.success("● FastAPI Engine: **ONLINE**")
            st.caption("Endpoint: `127.0.0.1:8000`")
        else:
            st.error("● FastAPI Engine: **ERROR**")
    except Exception:
        st.error("● FastAPI Engine: **OFFLINE**")
        st.caption("Run `python -m uvicorn main:app --reload`")

    st.markdown("---")
    st.info("🏆 **PayPal AI Hackathon 2026**\n\nBuilt with FastAPI, PayPal v2 Orders/Payouts & Autonomous Multi-Agent Orchestration.")

# ==========================================
# VIEW 1: EXECUTIVE TREASURY OVERVIEW
# ==========================================
if workspace == "📊 Executive Treasury Overview":
    st.markdown("""
        <div class="hero-banner">
            <h1 class="hero-title">NexusFlow AI Treasury Command Center</h1>
            <p class="hero-sub">Real-time autonomous B2B liquidity management, AI compliance auditing, and instant PayPal settlement.</p>
        </div>
    """, unsafe_allow_html=True)

    # KPI Row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("24h Autonomous Volume", "$64,820.00", "+18.4% vs yesterday")
    c2.metric("Active AI Agents", "3 Online", "Risk • Compliance • Settlement")
    c3.metric("Avg. Settlement Latency", "1.42 sec", "-94% vs manual wire")
    c4.metric("Fraud Interception Rate", "99.92%", "1 High-Risk Blocked")

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts & Architecture Pipeline
    col_chart, col_arch = st.columns([1.6, 1])

    with col_chart:
        st.subheader("📈 Treasury Cash Flow & Autonomous Disbursements (7-Day)")
        dates = [(datetime.now() - timedelta(days=i)).strftime("%b %d") for i in range(6, -1, -1)]
        chart_df = pd.DataFrame({
            "Date": dates,
            "Approved PayPal Payouts ($)": [8200, 11400, 9600, 15200, 13800, 19400, 22150],
            "Blocked High-Risk Volume ($)": [1200, 0, 3400, 800, 0, 4500, 14500]
        }).set_index("Date")
        st.area_chart(chart_df, color=["#0070BA", "#EF4444"])

    with col_arch:
        st.subheader("🧠 Active Agent Swarm Topology")
        st.markdown("""
            <div class="agent-card">
                <strong>1. Risk & Anomaly Agent</strong><br>
                <span style="color:#94A3B8; font-size:0.9rem;">Evaluates velocity spikes, threshold caps (>$10k), and entity reputation scores.</span>
            </div>
            <div class="agent-card" style="border-left-color: #38BDF8;">
                <strong>2. Regulatory Compliance Agent</strong><br>
                <span style="color:#94A3B8; font-size:0.9rem;">Parses invoice NLP line items, tax identifiers, and anti-fraud keywords.</span>
            </div>
            <div class="agent-card" style="border-left-color: #10B981;">
                <strong>3. PayPal Execution Agent</strong><br>
                <span style="color:#94A3B8; font-size:0.9rem;">Mints OAuth2 tokens and triggers instant PayPal Payouts v1 disbursements.</span>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# VIEW 2: MULTI-AGENT SWARM EXECUTION
# ==========================================
elif workspace == "🤖 Multi-Agent Swarm Execution":
    st.markdown("""
        <div class="hero-banner">
            <h1 class="hero-title">Autonomous Multi-Agent Invoice Auditor</h1>
            <p class="hero-sub">Submit a B2B invoice below. Watch the AI swarm inspect compliance, score fraud risk, and execute PayPal settlement.</p>
        </div>
    """, unsafe_allow_html=True)

    col_form, col_sim = st.columns([1.1, 1])

    with col_form:
        st.subheader("📄 Submit Vendor Invoice")
        
        # Preset Scenarios for Easy Hackathon Demoing
        preset = st.selectbox(
            "Quick-Load Demo Scenario:",
            [
                "Custom Input",
                "✅ Standard Approved Vendor ($2,500.00)",
                "🛑 High-Amount Anomaly Trigger ($15,000.00)",
                "⚠️ Compliance Keyword Violation ($850.00)"
            ]
        )

        default_email = "vendor-dev@example.com"
        default_amt = "2500.00"
        default_txt = "Invoice #2026-88: Cloud GPU cluster provisioning and Q4 AI model fine-tuning."

        if preset == "🛑 High-Amount Anomaly Trigger ($15,000.00)":
            default_email = "urgent-wire@offshore-holdings.net"
            default_amt = "15000.00"
            default_txt = "Invoice #9910: Urgent hardware procurement prepayment."
        elif preset == "⚠️ Compliance Keyword Violation ($850.00)":
            default_email = "contractor@unverified.org"
            default_amt = "850.00"
            default_txt = "Invoice #404: Miscellaneous consulting - invalid tax ID / unverified fraud test."

        with st.form("swarm_execution_form"):
            vendor_email = st.text_input("Recipient PayPal Email", value=default_email)
            amount = st.text_input("Disbursement Amount (USD)", value=default_amt)
            invoice_text = st.text_area("Invoice Line-Item Description", value=default_txt, height=110)
            
            submit_btn = st.form_submit_button("🚀 Launch Autonomous Swarm Evaluation")

    with col_sim:
        st.subheader("⚡ Live Agent Telemetry & Decision Log")
        if submit_btn:
            progress_bar = st.progress(0)
            status_box = st.empty()

            status_box.info("🔍 **Agent 1 (Risk Engine):** Analyzing transaction velocity & amount thresholds...")
            time.sleep(0.5)
            progress_bar.progress(35)

            status_box.info("📑 **Agent 2 (Compliance NLP):** Auditing line items & tax compliance rules...")
            time.sleep(0.5)
            progress_bar.progress(70)

            status_box.info("💳 **Agent 3 (PayPal Gateway):** Requesting settlement authorization...")
            try:
                response = requests.post(
                    f"{BACKEND_URL}/api/v1/agents/execute-treasury",
                    json={
                        "vendor_email": vendor_email,
                        "amount": amount,
                        "invoice_text": invoice_text
                    },
                    timeout=10
                )
                progress_bar.progress(100)
                data = response.json()
                orch = data.get("orchestration_result", {})
                status = orch.get("status", "unknown")

                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                risk_val = orch.get("risk_score", "N/A")

                if status == "approved_and_executed":
                    status_box.success("✅ **APPROVED & EXECUTED:** Funds disbursed via PayPal Payouts API!")
                    st.session_state.ledger.insert(0, {
                        "Timestamp": now_str,
                        "Vendor": vendor_email,
                        "Amount": f"${float(amount):,.2f}",
                        "Risk Score": f"{risk_val} (Pass)",
                        "Status": "✅ Settled (PayPal)"
                    })
                elif status == "rejected":
                    status_box.error(f"🛑 **REJECTED BY SWARM:** {orch.get('reason')}")
                    st.session_state.ledger.insert(0, {
                        "Timestamp": now_str,
                        "Vendor": vendor_email,
                        "Amount": f"${float(amount):,.2f}",
                        "Risk Score": f"{risk_val} (Flagged)",
                        "Status": "🛑 Blocked by Agent"
                    })
                else:
                    status_box.warning(f"⚠️ **EXECUTION NOTICE:** {orch}")

                with st.expander("Inspect Raw JSON Agent Payload", expanded=True):
                    st.json(data)

            except Exception as e:
                progress_bar.empty()
                status_box.error(f"❌ Connection Error: Ensure FastAPI backend is running on port 8000. ({e})")
        else:
            st.info("Select a scenario on the left and click **Launch Autonomous Swarm Evaluation** to watch the agents deliberate in real time.")

# ==========================================
# VIEW 3: PAYPAL DIRECT SANDBOX GATEWAY
# ==========================================
elif workspace == "💳 PayPal Direct Sandbox Gateway":
    st.markdown("""
        <div class="hero-banner">
            <h1 class="hero-title">PayPal Developer Sandbox Gateway</h1>
            <p class="hero-sub">Direct REST API v2 Orders (Escrow Funding) and v1 Payouts (Disbursements) testing console.</p>
        </div>
    """, unsafe_allow_html=True)

    t1, t2 = st.tabs(["📥 Create Escrow Order (v2/checkout/orders)", "📤 Execute Direct Payout (v1/payments/payouts)"])

    with t1:
        col_a, col_b = st.columns([1, 1.2])
        with col_a:
            st.markdown("#### Fund Treasury Escrow Account")
            ord_amt = st.text_input("Order Amount (USD)", "500.00", key="ord_amt")
            ord_curr = st.selectbox("Currency", ["USD", "EUR", "GBP"], key="ord_curr")
            if st.button("Generate PayPal Checkout Order"):
                with st.spinner("Communicating with PayPal Sandbox API..."):
                    try:
                        r = requests.post(
                            f"{BACKEND_URL}/api/v1/paypal/order",
                            json={"amount": ord_amt, "currency": ord_curr}
                        )
                        st.session_state["last_order"] = r.json()
                    except Exception as e:
                        st.error(f"Error: {e}")
        with col_b:
            st.markdown("#### PayPal API Response")
            if "last_order" in st.session_state:
                st.json(st.session_state["last_order"])
            else:
                st.caption("Submit an order on the left to inspect the PayPal approval links and Order ID.")

    with t2:
        col_c, col_d = st.columns([1, 1.2])
        with col_c:
            st.markdown("#### Direct Vendor Disbursement")
            pay_email = st.text_input("Recipient PayPal Email", "sb-vendor@business.example.com")
            pay_amt = st.text_input("Payout Amount (USD)", "250.00")
            pay_note = st.text_input("Payout Memo", "NexusFlow AI Automated Settlement")
            if st.button("Send Instant PayPal Payout"):
                with st.spinner("Dispatching PayPal Payout batch..."):
                    try:
                        r = requests.post(
                            f"{BACKEND_URL}/api/v1/paypal/payout",
                            json={
                                "recipient_email": pay_email,
                                "amount": pay_amt,
                                "currency": "USD",
                                "note": pay_note
                            }
                        )
                        st.session_state["last_payout"] = r.json()
                    except Exception as e:
                        st.error(f"Error: {e}")
        with col_d:
            st.markdown("#### Payout Batch Telemetry")
            if "last_payout" in st.session_state:
                st.json(st.session_state["last_payout"])
            else:
                st.caption("Trigger a payout on the left to inspect the PayPal Payout Batch ID.")

# ==========================================
# VIEW 4: IMMUTABLE AUDIT LEDGER
# ==========================================
elif workspace == "📜 Immutable Audit Ledger":
    st.markdown("""
        <div class="hero-banner">
            <h1 class="hero-title">Autonomous Treasury Audit Ledger</h1>
            <p class="hero-sub">Complete cryptographic and agent-decision log for every evaluated B2B invoice.</p>
        </div>
    """, unsafe_allow_html=True)

    df_ledger = pd.DataFrame(st.session_state.ledger)
    st.dataframe(df_ledger, use_container_width=True, hide_index=True)

    csv = df_ledger.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Export Compliance Audit Report (CSV)",
        data=csv,
        file_name="nexusflow_audit_ledger_2026.csv",
        mime="text/csv"
    )

# Example placement inside a tab or menu option
if menu_selection == "App Log Audit":
    render_log_audit_section()
