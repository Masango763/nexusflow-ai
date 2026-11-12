import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NexusFlow AI - Enterprise Treasury", layout="wide")

# Sidebar Navigation
st.sidebar.title("⚡ NEXUSFLOW AI")
st.sidebar.markdown("Autonomous Agentic Commerce Engine")
st.sidebar.markdown("---")

menu_selection = st.sidebar.radio(
    "COMMAND MODULES",
    [
        "Executive Treasury Overview",
        "Multi-Agent Swarm Execution",
        "PayPal Direct Sandbox Gateway",
        "Immutable Audit Ledger"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔌 Live System Telemetry")
st.sidebar.error("FastAPI Engine: ONLINE")

def render_log_audit_section():
    st.subheader("🛡️ Manage App Log Audit & Compliance Trail")
    st.markdown("Real-time telemetry and immutable audit logs for agent decisions, API calls, and transaction resolutions.")

    logs_data = [
        {"timestamp": "2026-11-12 21:14:02", "level": "INFO", "agent": "RiskAssessmentAgent", "event": "Evaluated transaction velocity for vendor #V-9021", "status": "APPROVED"},
        {"timestamp": "2026-11-12 21:13:50", "level": "WARNING", "agent": "ComplianceAuditor", "event": "Flagged missing tax identifier on invoice #INV-4402", "status": "FLAGGED"},
        {"timestamp": "2026-11-12 21:12:15", "level": "SUCCESS", "agent": "PayPalDisbursement", "event": "Executed v1 Payout for USD $4,500.00 via Sandbox", "status": "COMPLETED"},
        {"timestamp": "2026-11-12 21:10:05", "level": "INFO", "agent": "SystemCore", "event": "FastAPI session handshake validated securely", "status": "CONNECTED"}
    ]
    df_logs = pd.DataFrame(logs_data)

    col1, col2 = st.columns([2, 2])
    with col1:
        selected_level = st.selectbox("Filter by Log Level", ["ALL", "INFO", "WARNING", "SUCCESS", "ERROR"])
    with col2:
        search_query = st.text_input("Search audit logs", placeholder="Type keyword...")

    filtered_df = df_logs.copy()
    if selected_level != "ALL":
        filtered_df = filtered_df[filtered_df["level"] == selected_level]
    if search_query:
        filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]

    st.dataframe(filtered_df, use_container_width=True)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Full Audit Log (CSV)",
        data=csv_data,
        file_name=f"nexusflow_audit_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

# Main Content Routing
if menu_selection == "Executive Treasury Overview":
    st.title("📊 Executive Treasury Command Center")
    st.markdown("Monitor real-time system uptime, processed liquidity volume, and fraud mitigation statistics.")

elif menu_selection == "Multi-Agent Swarm Execution":
    st.title("🤖 Multi-Agent Swarm Execution")
    st.markdown("Run live agent workflows for automated risk assessment, compliance checking, and escrow creation.")

elif menu_selection == "PayPal Direct Sandbox Gateway":
    st.title("💳 PayPal Direct Sandbox Gateway")
    st.markdown("Test raw v2 Checkout Orders and v1 Payout requests directly against PayPal Sandbox APIs.")

elif menu_selection in ["Immutable Audit Ledger", "App Log Audit"]:
    render_log_audit_section()
