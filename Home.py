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
st.image('./pic/add.png')

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

dx=[dt1,dt2,dt3,dt4]
dx2=pd.DataFrame(dx,index=["dt1","dt2","dt3","dt4""dt5","dt6","dt7","dt8"])


if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.pie_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8="""
<div style="background-color:#B160EC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลการเป็นโรคหัวใจ</h5></center>
</div>
"""

st.markdown(html_8,unsafe_allow_html=True)
st.markdown("")

st_len = st.slider("กรุณาเลือกข้อมูล Pregnancies")
sd = st.slider("กรุณาเลือกข้อมูล Glucose")
pt_len = st.number_input("กรุณาเลือกข้อมูล BloodPressure")
wd = st.number_input("กรุณาเลือกข้อมูล SkinThickness")
pt_len = st.number_input("กรุณาเลือกข้อมูล Insulin")
wd = st.number_input("กรุณาเลือกข้อมูล BMI")
wd = st.number_input("กรุณาเลือกข้อมูล DiabetesPedigreeFunction")
pt_len = st.number_input("กรุณาเลือกข้อมูล Age")

if  st.button("ทำนายผล]"):
    loaded_model = pickle.load(open('./data/trained_model.sav', 'rb'))
    input_data =  (st_len,sd,pt_len,wd)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    st.write(prediction[0])
    if prediction == '1':
        st.image('./pic/versicolor.jpg')
    elif prediction == '0':
        st.image('./pic/virginica.jpg')
        st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงผลการทำนาย")



