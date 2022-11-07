import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle


html_8="""
<div style="background-color:#B160EC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลการเป็นโรคหัวใจ</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv("./data/diabetes.csv")
st.write(dt.head(10))

dt1=dt['Pregnancies'].sum()
dt2=dt['Glucose'].sum()
dt3=dt['BloodPressure'].sum()
dt4=dt['SkinThickness'].sum()
dt5=dt['Insulin'].sum()
dt6=dt['BMI'].sum()
dt7=dt['DiabetesPedigreeFunction'].sum()
dt8=dt['Age'].sum()
dx=[dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8]
dx2=pd.DataFrame(dx,index=["dt1","dt2","dt3","dt4","dt5","dt6","dt7","dt8"])
