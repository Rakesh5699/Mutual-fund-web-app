import streamlit as st
from mftool import Mftool
import pandas as pd

mf = Mftool()
st.title("Mutual Funds Financial dashbaord")

option = st.sidebar.selectbox(
    "Choose a action",
    ['View Available Schemes','Scheme Details','Historical Nav']
)

schema_codes = {v:k for k,v in mf.get_scheme_codes().items()}

if option == 'View Available Schemes':
    st.sidebar.header('View Available Schemes')
    user_input = st.sidebar.text_input("",placeholder="Enter AMC Name")
    search_scheme = st.sidebar.button("🔍 Search")
    if user_input or search_scheme:
        schemes = mf.get_available_schemes(user_input)
        st.write(pd.DataFrame(list(schemes.items()), columns=["Scheme Name", "Scheme Code"]) if schemes else "No records found")

if option == 'Scheme Details':
    st.sidebar.header('Scheme Details')
    schema_code = schema_codes[st.sidebar.selectbox("Select a scheme",schema_codes.keys())]
    search_code = st.sidebar.button("🔍 Search")
    if search_code:
        data = mf.get_scheme_details(schema_code)
        st.markdown(
        f"""
        <div style="
            background-color: #f7f9fc;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            width: 80%;
        ">
            <h4 style="color:#1f77b4; margin-bottom:10px;">{data['scheme_name']}</h4>
            <p><b>🏦 Fund House:</b> {data['fund_house']}</p>
            <p><b>📂 Scheme Type:</b> {data['scheme_type']}</p>
            <p><b>📊 Category:</b> {data['scheme_category']}</p>
            <p><b>💳 Scheme Code:</b> {data['scheme_code']}</p>
            <p><b>📅 Start Date:</b> {data['scheme_start_date']['date']}</p>
            <p><b>💰 NAV on Start Date:</b> {data['scheme_start_date']['nav']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
if option == "Historical Nav":
    st.sidebar.header('Historical Nav')
    schema_code = schema_codes[st.sidebar.selectbox("Select a scheme",schema_codes.keys())]
    search_code = st.sidebar.button("🔍 Search")
    if search_code:
        nav_hist = mf.get_scheme_historical_nav(schema_code,as_Dataframe=True)
        st.write(nav_hist)