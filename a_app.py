import streamlit as st
import utils

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = 'Convert Oracle SQL Queries to Netezza SQL'
    , page_icon = ':office:'
    , layout = 'wide')

st.title('Convert Oracle SQL Queries to Netezza SQL')


# ---- SIDEBAR ----
options = ['', 'TRUNC']

example = st.sidebar.selectbox(label = 'Examples', options = options)

default_query = ''

if example == 'TRUNC':
    default_query = utils.load_trunc_example()
    documentation = 'https://www.ibm.com/docs/en/ias?topic=functions-date-trunc'

# ---- BODY ----
left_column, right_column = st.columns(2)
with left_column:
    st.subheader('Oracle SQL Query')
    oracle_query = st.text_area(label = 'Oracle SQL Query'
        , value = default_query)

    oracle_query = utils.convert_trunc(oracle_query)

convert = st.button('Convert Query')

with right_column:
    st.subheader('Netezza SQL Query')

    if convert:
        oracle_query = st.text_area(label = 'Netezza SQL Query'
        , value = oracle_query)

if example:
    st.subheader('Helpful links:')
    st.write(documentation)

# Hide Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html = True)
