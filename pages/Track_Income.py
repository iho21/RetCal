import streamlit as st
import pandas as pd

st.title('Net Worth Tracker')

# Input fields for assets
cash = st.number_input('Cash', value=0.0)
investments = st.number_input('Investments', value=0.0)
real_estate = st.number_input('Real Estate', value=0.0)
other_assets = st.number_input('Other Assets', value=0.0)

# Calculate total assets
total_assets = cash + investments + real_estate + other_assets

# Input fields for liabilities
mortgage = st.number_input('Mortgage', value=0.0)
loans = st.number_input('Loans', value=0.0)
credit_card_debt = st.number_input('Credit Card Debt', value=0.0)
other_liabilities = st.number_input('Other Liabilities', value=0.0)

# Calculate total liabilities
total_liabilities = mortgage + loans + credit_card_debt + other_liabilities

# Calculate net worth
net_worth = total_assets - total_liabilities

# Display net worth
st.write(f'Net Worth: ${net_worth}')
