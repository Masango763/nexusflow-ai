import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="NexusFlow AI - PayPal AI Hackathon Edition", layout="wide")

# Custom Dark Fintech Glassmorphic Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid #334155;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("### 💳 **PayPal**")
st.sidebar.markdown("### ⚡ NEXUSFLOW AI")
st.sidebar.markdown("PayPal AI Hackathon Edition")
st.sidebar.markdown("---")

st.sidebar.markdown("**COMMAND MODULES**")
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

def render_executive_overview():
    st.markdown("""
        <div class="main-card">
            <h1 style='color: #60a5fa;'>Treasury Command Center</h1>
            <p style='color: #94a3b8;'>Autonomous B2B liquidity & compliance auditing.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Volume Processed", "$64,820.00", "+18.4%")
    with col2:
        st.metric("Active Agents", "3 Online", "Optimal")
    with col3:
        st.metric("Blocked Disputed Txns", "1 Pending", "Action Required")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Graph representing volume trends & risk metrics
    st.markdown("### 📈 Real-Time Liquidity & Risk Velocity")
    chart_data = pd.DataFrame({
        "Date": ["Nov 06", "Nov 07", "Nov 08", "Nov 09", "Nov 10", "Nov 11", "Nov 12"],
        "Approved Payouts ($)": [8200, 12500, 15400, 11200, 18900, 21400, 24500],
        "Blocked High-Risk Volume ($)": [1200, 4500, 800, 3100, 1500, 4200, 2100]
    })
    
    fig = px.area(
        chart_data, 
        x="Date", 
        y=["Approved Payouts ($)", "Blocked High-Risk Volume ($)"],
        color_discrete_map={"Approved Payouts ($)": "#3b82f6", "Blocked High-Risk Volume ($)": "#ef4444"},
        template="plotly_dark"
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

def render_audit_ledger():
    st.markdown("""
        <div class="main-card">
            <h1 style='color: #60a5fa;'>Immutable Audit Ledger</h1>
            <p style='color: #94a3b8;'>Complete cryptographic activity log.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

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

# Main Content Routing
if menu_selection == "Executive Overview":
    render_executive_overview()

elif menu_selection == "Multi-Agent Swarm":
    st.markdown("""
        <div class="main-card">
            <h1 style='color: #60a5fa;'>Agentic Invoice Auditor</h1>
            <p style='color: #94a3b8;'>Simulate risk evaluation & automated settlement.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.text_input("Vendor Email", value="partner@business.com")
    st.text_input("Amount ($)", value="2500.00")
    if st.button("Run Multi-Agent Swarm Evaluation"):
        st.success("Risk Assessment Agent: Passed (Score 0.04) | PayPal Payout v1 Queued Successfully!")

elif menu_selection == "Disputes & Appeals Queue":
    st.markdown("""
        <div class="main-card">
            <h1 style='color: #60a5fa;'>Disputes & Appeals Review Queue</h1>
            <p style='color: #94a3b8;'>Manually review, override, and force-settle transactions flagged by the Risk Agent.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("⚠️ 1 High-Risk Transaction Flagged for Manual Review")
    if st.button("Force-Override & Approve Payout"):
        st.success("Transaction override logged to immutable audit trail.")

elif menu_selection == "Audit Ledger":
    render_audit_ledger()
