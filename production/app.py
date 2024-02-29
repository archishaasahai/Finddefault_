import streamlit as st
import numpy as np
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder, StandardScaler

import pickle

st.set_page_config(page_title="Credit Card Fraud Detection System", page_icon="💰")

st.title('Credit Card Fraud Detection System')


with open('clf.pkl', 'rb') as f:
    rf = pickle.load(f)

with open('iqr_thresholds.json', 'rb') as infile : 
    iqr = json.load(infile)
 
    
with st.container() : 
    text1, text2, text3, text4, text5 = st.columns(5)
    with text1 : 
        v1 = st.number_input("V1", value = 1.59364)

    with text2 : 
        v2 = st.number_input("V2", value = -0.29739)

    with text3 : 
        v3 = st.number_input("V3", value = -1.274873)

    with text4 : 
        v4 = st.number_input("V4", value = 2.967524)

    with text5 : 
        v5 = st.number_input("V5", value = 2.195722)
        

with st.container() : 
    text1, text2, text3, text4, text5 = st.columns(5)
    with text1 : 
        v6 = st.number_input("V6", value = 2.383457)

    with text2 : 
        v7 = st.number_input("V7", value = -0.992858)

    with text3 : 
        v9 = st.number_input("V9", value = 0.636032)

    with text4 : 
        v10 = st.number_input("V10", value = 1.016501)

    with text5 : 
        v11 = st.number_input("V11", value = 0.502974)


with st.container() : 
    text1, text2, text3, text4, text5 = st.columns(5)
    with text1 : 
        v12 = st.number_input("V12", value = -2.753744)

    with text2 : 
        v14 = st.number_input("V14", value = 1.565899)

    with text3 : 
        v16 = st.number_input("V16", value = 1.317002)

    with text4 : 
        v17 = st.number_input("V17", value = -0.443271)

    with text5 : 
        v18 = st.number_input("V18", value = 0.298609)

with st.container() : 
    text1, text2 = st.columns(2)
    with text1 : 
        v19 = st.number_input("V19", value = -2.262994)

    with text2 : 
        v20 = st.number_input("V20", value = 0.054537)


def cvt_iqr(val, type_val):
    return iqr[type_val]['upper_bound'] if val >= iqr[type_val]['upper_bound'] else iqr[type_val]['lower_bound'] if val<= iqr[type_val]['lower_bound'] else val

if st.button("Check Fraud") :
    # print(np.array([1,2,3]).reshape(-1,1).shape)
    # print(iqr)
    input_coming = np.array([
        cvt_iqr(v1, "V1"), cvt_iqr(v2, "V2"), cvt_iqr(v3, "V3"), cvt_iqr(v4, "V4"), cvt_iqr(v5, "V5"),
        cvt_iqr(v6,"V6"), cvt_iqr(v7, "V7"), cvt_iqr(v9, "V9"), cvt_iqr(v10, "V10"), cvt_iqr(v11, "V11"), cvt_iqr(v12, "V12"), cvt_iqr(v14, "V14"), cvt_iqr(v16, "V16"), cvt_iqr(v17, "V17"), cvt_iqr(v18, "V18"), cvt_iqr(v19, "V19"), cvt_iqr(v20, "V20")
    ]).reshape(1,-1)

    y_pred = rf.predict(input_coming)
    # print(y_pred)

    st.write(f"### Prediction : {'Fraud' if y_pred[0] else 'Not Fraud'}")

