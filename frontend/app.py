import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="NexusFlow AI | Enterprise Agentic Treasury",
    page_icon="⚡",
    layout="wide"
)

if "ledger" not in st.session_state:
    st.session_state.ledger = [
        {"Timestamp": "2026-11-12 09:14:22", "Vendor": "cloud-ops@aws-partner.io", "Amount": "$4,200.00", "Risk Score": "0.08 (Low)", "Status": "✅ Settled (PayPal)"},
        {"Timestamp": "2026-11-12 11:30:51", "Vendor": "unknown-offshore@shell.biz", "Amount": "$14,500.00", "Risk Score": "0.89 (High)", "Status": "🛑 Blocked by Risk Agent"},
    ]

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0B1120 0%, #0F172A 100%); color: #F8FAFC; }
    .hero-banner { background: linear-gradient(90deg, rgba(0, 48, 135, 0.45) 0%, rgba(0, 112, 186, 0.25) 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 14px; padding: 1.75rem 2rem; margin-bottom: 1.5rem; }
    .hero-title { font-size: 2.2rem; font-weight: 800; background: linear-gradient(90deg, #38BDF8, #818CF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; }
    .hero-sub { color: #94A3B8; font-size: 1.05rem; margin-top: 0.4rem; }
    
    div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-weight: 800 !important;
        font-size: 1.8rem !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #CBD5E1 !important;
        font-weight: 600 !important;
    }
    .stButton > button { background: linear-gradient(90deg, #0070BA 0%, #003087 100%); color: white; border: none; border-radius: 8px; padding: 0.6rem 1.5rem; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

with st.sidebar:
    st.image("https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg", width=70)
    st.markdown("## ⚡ **NEXUSFLOW AI**")
    st.caption("PayPal AI Hackathon Edition")
    st.markdown("---")
    workspace = st.radio("COMMAND MODULES", ["📊 Executive Overview", "🤖 Multi-Agent Swarm", "⚖️ Disputes & Appeals Queue", "📜 Audit Ledger"])

if workspace == "📊 Executive Overview":
    st.markdown('<div class="hero-banner"><h1 class="hero-title">Treasury Command Center</h1><p class="hero-sub">Autonomous B2B liquidity & compliance auditing.</p></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Volume Processed", "$64,820.00", "+18.4%")
    c2.metric("Active Agents", "3 Online", "Optimal")
    c3.metric("Blocked Disputed Txns", "1 Pending", "Action Required")

elif workspace == "🤖 Multi-Agent Swarm":
    st.markdown('<div class="hero-banner"><h1 class="hero-title">Agentic Invoice Auditor</h1><p class="hero-sub">Simulate risk evaluation & automated settlement.</p></div>', unsafe_allow_html=True)
    with st.form("swarm_form"):
        email = st.text_input("Vendor Email", "partner@business.com")
        amt = st.text_input("Amount ($)", "3500.00")
        desc = st.text_area("Invoice Description", "Cloud infrastructure maintenance.")
        if st.form_submit_button("Run Swarm"):
            st.success("Transaction evaluated and approved by Agent Swarm!")

elif workspace == "⚖️ Disputes & Appeals Queue":
    st.markdown('<div class="hero-banner"><h1 class="hero-title">Disputes & Appeals Review Queue</h1><p class="hero-sub">Manually review, override, and force-settle transactions flagged by the Risk Agent.</p></div>', unsafe_allow_html=True)
    st.warning("⚠️ **1 High-Risk Transaction Flagged for Manual Review**")
    col_info, col_action = st.columns([1.5, 1])
    with col_info:
        st.markdown("### Flagged Transaction Details")
        st.json({"transaction_id": "TXN-9910-REF", "vendor": "unknown-offshore@shell.biz", "amount": "$14,500.00", "risk_score": 0.89, "flag_reason": "Exceeds standard velocity threshold."})
    with col_action:
        st.markdown("### Administrator Override")
        admin_note = st.text_input("Override Justification Memo", "Manual KYC verified.")
        if st.button("🔓 Approve Appeal & Force Payout"):
            st.success("Appeal approved! Payout dispatched via PayPal.")

elif workspace == "📜 Audit Ledger":
    st.markdown('<div class="hero-banner"><h1 class="hero-title">Immutable Audit Ledger</h1><p class="hero-sub">Complete cryptographic activity log.</p></div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(st.session_state.ledger), use_container_width=True, hide_index=True)

# Safe menu routing fallback
if "menu_selection" in locals() and menu_selection in ["Immutable Audit Ledger", "App Log Audit"]:
    render_log_audit_section()
