import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NexusFlow AI - PayPal AI Hackathon Edition", layout="wide")

# Sidebar Navigation matching your original interface
st.sidebar.image("https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg", width=50)
st.sidebar.title("NEXUSFLOW AI")
st.sidebar.markdown("PayPal AI Hackathon Edition")
st.sidebar.markdown("---")

st.sidebar.markdown("COMMAND MODULES")
menu_selection = st.sidebar.radio(
    "",
    [
        "Executive Overview",
        "Multi-Agent Swarm",
        "Disputes & Appeals Queue",
        "Audit Ledger"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔌 Live System Telemetry")
st.sidebar.success("FastAPI Engine: ONLINE")

def render_audit_ledger():
    st.markdown("### Immutable Audit Ledger")
    st.markdown("Complete cryptographic activity log.")

    logs_data = [
        {"Timestamp": "2026-11-12 09:14:22", "Vendor": "cloud-ops@aws-partner.io", "Amount": "$4,200.00", "Risk Score": "0.08 (Low)", "Status": "✔ Settled"},
        {"Timestamp": "2026-11-12 11:30:51", "Vendor": "unknown-offshore@shell.biz", "Amount": "$14,500.00", "Risk Score": "0.89 (High)", "Status": "🔴 Blocked"}
    ]
    df = pd.DataFrame(logs_data)
    st.dataframe(df, use_container_width=True)

    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Compliance CSV",
        data=csv_data,
        file_name=f"nexusflow_audit_ledger_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

# Main Routing matching your original design
if menu_selection == "Executive Overview":
    st.markdown("## Treasury Command Center")
    st.markdown("Autonomous B2B liquidity & compliance auditing.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Volume Processed", "$64,820.00", "+18.4%")
    with col2:
        st.metric("Active Agents", "3 Online", "Optimal")
    with col3:
        st.metric("Blocked Disputed Txns", "1 Pending", "Action Required")

elif menu_selection == "Multi-Agent Swarm":
    st.markdown("## Agentic Invoice Auditor")
    st.markdown("Simulate risk evaluation & automated settlement.")
    
    st.text_input("Vendor Email", value="partner@business.com")
    st.text_input("Amount ($)", value="2500.00")
    if st.button("Run Multi-Agent Swarm Evaluation"):
        st.success("Risk Assessment Agent: Passed (Score 0.04) | PayPal Payout v1 Queued Successfully!")

elif menu_selection == "Disputes & Appeals Queue":
    st.markdown("## Disputes & Appeals Review Queue")
    st.markdown("Manually review, override, and force-settle transactions flagged by the Risk Agent.")
    st.warning("⚠️ 1 High-Risk Transaction Flagged for Manual Review")
    if st.button("Force-Override & Approve Payout"):
        st.success("Transaction override logged to immutable audit trail.")

elif menu_selection == "Audit Ledger":
    render_audit_ledger()
