import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


html_8="""
<div style="background-color:#B160EC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

dt=pd.read_csv("./data/iris.csv")
st.write(dt.head(10))

dt1=dt['petal.length'].sum()
dt2=dt['petal.width'].sum()
dt3=dt['sepal.length'].sum()
dt4=dt['sepal.width'].sum()
dx=[dt1,dt2,dt3,dt4]
dx2=pd.DataFrame(dx,index=["dt1","dt2","dt3","dt4"])


if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.pie_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8="""
<div style="background-color:#B160EC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

st_len = st.slider("กรุณาเลือกข้อมูล sepal.length")
sd = st.slider("กรุณาเลือกข้อมูล sepal.width")
pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
wd = st.slider("กรุณาเลือกข้อมูล petal.width")

if  st.button("ทำนายผล]"):
    st.markdown("ใส่โมเดล")
    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงผลการทำนาย")
    