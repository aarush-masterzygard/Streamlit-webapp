import streamlit as st
import pandas as pd
import numpy as np

st.markdown("<h1 style='color:red'>My Cool Chart</h1>", unsafe_allow_html=True)



chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)