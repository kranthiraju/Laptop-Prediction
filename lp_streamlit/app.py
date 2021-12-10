import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('../laptop jy/pipe.pkl','rb'))
laptop = pickle.load(open('../laptop jy/laptop_data_pkl.pkl','rb'))

st.title('Laptop Prediction')

company = st.selectbox('Brand',laptop['Company'].unique())

typename = st.selectbox('Type',laptop['TypeName'].unique())

cpu = st.selectbox('Processor',laptop['Cpu'].unique())

ram = st.selectbox('RAM (in GB)',sorted(laptop['Ram'].unique()))

memory = st.selectbox('Memory (in GB)',[0,128,256,512,1024,2048])

gpu = st.selectbox('GPU Brand',laptop['Gpu'].unique())

os = st.selectbox('Operating System',laptop['OpSys'].unique())

weight = st.number_input('Weight in KG')

touch = st.selectbox('TouchScreen',['Yes','No'])

ips = st.selectbox('IPS',['Yes','No'])

screen_size = st.number_input('Screensize')

resolution = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x1800','3200x1800','2880x1800','2560x1600','2560x1440','2340x1440'])

if st.button('Predict Price'):
    ppi =(((int(resolution.split('x')[0])**2)+(int(resolution.split('x')[1])**2))**0.5)/screen_size
    if touch=='Yes':
        touch=1
    else:
        touch=0

    if ips=='Yes':
        ips=1
    else:
        ips=0
    query = np.array([company,typename,cpu,ram,memory,gpu,os,weight,touch,ips,ppi])
    query = query.reshape(1,11)

    st.title('The Prediction Price Value is '+str(int(np.exp(pipe.predict(query)))))
