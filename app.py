import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import pandas as pd
import requests
from datetime import datetime




# upload the Excel file to my cloud URL
address1 = "60 Tiffany Pl, Brooklyn, NY 11231, USA"


label = "Please upload your Excel File:"



def upload_file(url) -> tuple:
    '''
    This function returns the url and the sheets names to the app interface to get them verified
    '''
    try:
        #uploading and run the do thd do
        #do the do
        pass
    except ValueError:
        print("error loading your file..")

if st.button("Predict"):
    st.write(upload_file())
else:
    st.write("Something went wrong")

#verify sheets:
label = "Please Verify sheet names in your Excel File:"

def verify_sheets(sheet_names:dict) -> dict:
    '''
    This function will place the sheets found in the excel files in an input form,
        for the user to confirm. if a sheet has another name it will be placed as a warning:
        Please rename your sheets as the following: Murs, Sols, Poteaux, Poutres.
    '''
    #we can translate to french if OK

    sheet_murs = st.text_input('Walls Sheet', value=sheet_names['murs'])
    sheet_sols = st.text_input('Platform Sheet', value=sheet_names['sols'])
    sheet_poteaux = st.text_input('Posts Sheet', value=sheet_names['murs'])
    sheet_Poutres = st.text_input('Beams Sheet', value=sheet_names['poutres'])

    sheet_names_verified = {
        'murs' : sheet_murs,
        'sols':sheet_sols,
        'murs':sheet_poteaux,
        'poutres':sheet_Poutres
        }

    return sheet_names_verified


#calling our Fast API
# EXAMPLE HERE: http://127.0.0.1:8000/predict?file=someurl&sheets=someparams

def call_api():

    api_base = 'https://apiurl/predict?'

    file = 'file_url'
    sheets = verify_sheets(file)

    #run some progression bar here


    #run api here
    bim_api_call = f'{api_base}pickup_datetime={file}&sheets={sheets}'

    return print("API CALLED OK")

if st.button("Predict"):
    st.write(call_api())
else:
    st.write("Waiting for user input")

import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
