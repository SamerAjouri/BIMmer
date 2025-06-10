import streamlit as st
import streamlit.components.v1 as components
import logging
import numpy as np
import pandas as pd


import requests
import os
import sys
import time

#from google.cloud import storage
from io import StringIO

#st.set_page_config(layout="wide")

#default for testing
sheet_names = {'murs':'murs','sols':'sols','poteaux':'poteaux','poutres':'poutres'}

#FUNCTIONS
def verify_sheets(file_name):
    '''
    This function will place the sheets found in the excel files in an input form,
    for the user to confirm. if a sheet has another name it will be placed as a warning:
    Please rename your sheets as the following: Murs, Sols, Poteaux, Poutres.
    '''
    pass



def upload_file(file_name):
    '''
    This function will write the file to /data/raw in the main app
    '''
    api_call = f'http://127.0.0.1:8001/upload_excel?file=@{file_name}'

    try:
        data = requests.get(api_call)
        st.write(data)

        return 'all is ok..'
    except ValueError:
        return "error loading your file.."

st.image('image/background.png')
st.title('BIMmer!')
st.subheader("A BIM prediciton tool for Autodesk Revit®", divider="gray")

tab1, tab2, tab3 = st.tabs(["About BIMmer", "Predict", "Notes"])
with tab1:
    st.markdown('''
        BIM plays a crucial role in modern construction, enabling better planning,
        reduced costs, and improved collaboration.
        Predicting BIM attributes accurately can enhance decision-making, improve
        resource allocation, and drive innovation within Eiffage's projects.''')
    st.markdown('''
                This project aims to leverage machine learning techniques to predict
                Building Information Modeling (BIM) outcomes for a leading construction
                company in France.
                It dies so by analyzing construction data, material properties.
        ''')

with tab2:
    st.markdown('''
        Upload a file to start..''')

with tab3:
    st.markdown('''
        Disclaimer text goes in here.. \n
        Image by [ Eglantine Shala](https://pixabay.com/users/eglantineshala-11648844/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9014868) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9014868)''')

uploaded_file = st.file_uploader(label = "Choose a file to upload",
                                    #key='uploaded_excel',
                                    type="xlsx",
                                    #on_change=hide_uploader,
                                    accept_multiple_files=False,
                                    )

if uploaded_file is not None:
    #progeress
    with st.spinner("Reading sheet names inside your file...", show_time=True):
        time.sleep(0)

        #Verifying sheets
        #sheets to check = ['murs', 'sols', 'poutres', 'poteaux']
        try:
            file = pd.ExcelFile(uploaded_file)
            sheet_names =  file.sheet_names
            stat = True

            for sheet in sheet_names:
                if sheet.lower() in ['murs', 'sols', 'poutres', 'poteaux']:
                    st.write(f'sheet: {sheet} is OK .. \n')
                else:
                    st.write(f'sheet: {sheet} is not OK .. \n')
                    st.write(f'please fix names of sheets')
                    stat = False

        except Exception as e:
            st.write(f"Error loading sheets from file: {e}")

    if stat == True:
        st.success(f"You have the correct sheets in your file..")

        if st.button("BIM predict your data."):
            api_call = f'http://127.0.0.1:8001/upload_excel?file={uploaded_file}'
            st.write(api_call)

            try:
                files = {'file': uploaded_file}  # Specify the file you want to upload
                response = requests.post('http://127.0.0.1:8001/upload_excel', files=files)

                #data = requests.get(api_call)
                st.write(response)
            except ValueError:
                st.write("error loading your file..")
    else:
        st.success(f"You're out of luck! Please fix the name(s) of your excel sheets")

