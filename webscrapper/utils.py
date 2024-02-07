from urllib.request import Request, urlopen
import streamlit as st
import pandas as pd
import base64


@st.cache_data
def load_data(year):
    req = Request(url="https://www.hockey-reference.com/leagues/NHL_" + str(year) + '_skaters-advanced.html',
                  headers={'User-Agency': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = pd.read_html(webpage, header=1)
    df = html[0]
    df = df.drop(df[df.Age == 'Age'].index)  # Deletes repeating headers in content
    df = df.fillna(0)
    df = df.drop(['Rk'], axis=1)
    return df


def file_load(df):
    csv_file = df.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv_file;base64,{b64}" download="stats.csv"> Download CSV File</a>'
    return href
