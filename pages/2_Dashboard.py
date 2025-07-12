import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""
    <h1 style='color:#4B8BBE; text-align:center;'>Dashboard</h1>
    <hr>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Users", "1,024", "+24")
col2.metric("Revenue", "$8,500", "+$500")
col3.metric("Conversion Rate", "5.2%", "+0.3%")

# Chart
st.markdown("<h3 style='color:#4B8BBE;'>Activity Overview</h3>", unsafe_allow_html=True)
chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=["Product A", "Product B", "Product C"]
)
st.line_chart(chart_data)

# Summary
st.markdown("""
    <div style='padding: 15px; background: #222; border-radius: 10px; color: #fff;'>
        <h4>Summary</h4>
        <p style='font-size:15px;'>Performance is trending upward this month. Keep up the great work!</p>
    </div>
""", unsafe_allow_html=True)