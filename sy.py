import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

html_21="""
<div style="background-color: #E7CE5B ;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
 <center><h3>การวิเคราะห์รายบุคคล</h3></center>
</div>
"""
st.image('./pic/ban21.png')
st.markdown(html_21,unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.sidebar.markdown("# วิเคราะห์รายบุคคล ")
