import streamlit as st
import webbrowser
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1)

websites = ['onemileatatime.com',
            'creditcardgenius.ca',
            # 'www.greedyrates.ca',
            # 'princeoftravel.com',
            # 'www.pointsnerd.ca',
            # 'travelupdate.com',
            # 'www.flyertalk.com',
            'www.executivetraveller.com']

st.header("Aeroplan: Key Site Search")

with st.form('aeroplan site search'):
    date_range = st.date_input('Date Range', (yesterday, today))

    kw1 = st.text_input('Keyword 1', 'aeroplan')
    kw2 = st.text_input('Keyword 2')
    kw3 = st.text_input('Keyword 3')

    submitted = st.form_submit_button('Submit')

if submitted:

    keywords = f'{kw1}'
    if len(kw2) > 0:
        keywords += f'+{kw2}'
    if len(kw3) > 0:
        keywords += f'+{kw3}'

    start_date = date_range[0].strftime("%m/%d/%Y")
    end_date = date_range[1].strftime("%m/%d/%Y")

    for website in websites:
        target_url = f'https://www.google.com/search?as_sitesearch={website}&q={keywords}&tbs=cdr:1,cd_min:{start_date},cd_max:{end_date}'
        # st.write(target_url)
        webbrowser.open_new_tab(target_url)


