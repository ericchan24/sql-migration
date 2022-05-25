import streamlit as st
import utils
# import importlib
# importlib.reload(utils)

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = 'Convert Oracle SQL Queries to Netezza SQL'
    , page_icon = ':office:'
    , layout = 'wide')

st.title('Convert Oracle SQL Queries to Netezza SQL')


# ---- SIDEBAR ----
options = [
    ''
    , 'dual'
    , 'PIVOT'
    , 'SYSDATE'
    , 'TO_NUMBER'
    , 'TRUNC']

example = st.sidebar.selectbox(label = 'Examples', options = options)

default_query = ''

if example == 'dual':
    oracle_query = utils.load_example_dual()
    netezza_query = utils.load_converted_dual()
    documentation = [
        'https://stackoverflow.com/questions/37850503/what-is-the-name-of-default-dual-table-in-netezza'
        , 'https://dwgeek.com/netezza-dual-table-alternative.html'
        ]
    
if example == 'PIVOT':
    oracle_query = utils.load_example_pivot()
    netezza_query = utils.load_converted_pivot()
    documentation = [
        'https://www.ibm.com/support/pages/netezza-does-not-support-pivot-and-unpivot-operations-sql'
        , 'https://dwgeek.com/netezza-pivot-rows-column-example.html'
        ]

if example == 'SYSDATE':
    oracle_query = utils.load_example_sysdate()
    netezza_query = utils.load_converted_sysdate()
    documentation = [
        'https://dwgeek.com/netezza-date-functions-examples.html'
        , 'https://www.ibm.com/docs/en/psfa/7.2.1?topic=reference-functions'
        ]

if example == 'TO_NUMBER':
    oracle_query = utils.load_example_to_number()
    netezza_query = utils.load_converted_to_number()
    documentation = [
        'https://www.ibm.com/docs/en/psfa/7.2.1?topic=constants-data-types-aliases'
        ]

if example == 'TRUNC':
    oracle_query = utils.load_example_trunc()
    netezza_query = utils.load_converted_trunc()
    documentation = [
        'https://www.ibm.com/docs/en/ias?topic=functions-date-trunc'
        ]

# ---- BODY ----
left_column, right_column = st.columns(2)

if example:
    with left_column:
        st.subheader('Oracle SQL Query')
        oracle_query = st.text_area(label = 'Oracle SQL Query'
            , value = oracle_query
            , height = 400)

    with right_column:
        st.subheader('Netezza SQL Query')

        oracle_query = st.text_area(label = 'Netezza SQL Query'
        , value = netezza_query
        , height = 400)

    st.subheader('Helpful links:')
    for doc in documentation:
        st.write(doc)

# Hide Streamlit branding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html = True)
