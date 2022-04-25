import streamlit as st
import webbrowser
from datetime import date
from datetime import timedelta

st. set_page_config(layout="wide")

today = date.today()
yesterday = today - timedelta(days = 1)


websites = ['flytrippers.com',
'winstonsih.com/category/travel',
'milesopedia.com/en/category/news',
'www.moneywehave.com',
'travelupdate.com/blogger/pointsmilesandbling',
'www.pointsnerd.ca',
'www.pointsnerd.ca',
'princeoftravel.com/blog',
'onemileatatime.com',
'www.rewardscanada.ca',
'www.ratehub.ca/blog',
'www.nerdwallet.com',
'www.greedyrates.ca',
'creditcardgenius.ca/blog',
'www.godsavethepoints.com',
'pizzainmotion.boardingarea.com',
'thepointsguy.co.uk/news',
'thepointsguy.com/all',
'www.travelcodex.com',
'viewfromthewing.com',
'blog.wandr.me',
'canadapointsguy.com',
'awardwallet.com',
'thriftytraveler.com',
'www.cnn.com/cnn-underscored',
'www.cnbc.com/select',
'www.google.ca']

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

    all_links = ""
    for website in websites:
        target_url = f'www.google.com/search?as_sitesearch={website}&q={keywords}&tbs=cdr:1,cd_min:{start_date},cd_max:{end_date}'
        # all_links += target_url + '\n'
        st.write(target_url)
        webbrowser.open_new_tab(target_url)

    # st.write(all_links)



