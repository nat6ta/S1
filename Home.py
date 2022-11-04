import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pickle


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
pt_len = st.number_input("กรุณาเลือกข้อมูล petal.length")
wd = st.number_input("กรุณาเลือกข้อมูล petal.width")

if  st.button("ทำนายผล]"):
    loaded_model = pickle.load(open('./data/trained_model.sav', 'rb'))
    input_data =  (st_len,sd,pt_len,wd)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction[0])
    st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงผลการทำนาย")



