import streamlit as st
import pandas as pd
import numpy as np
st.title('Net Worth Tracker')

# Input fields for assets
cash = st.number_input('Cash', value=0.0)
investments = st.number_input('Investments', value=0.0)
real_estate = st.number_input('Real Estate', value=0.0)
other_assets = st.number_input('Other Assets', value=0.0)

# Input fields for monthly income from different accounts
account1 = st.number_input('Monthly Income from Account 1', value=0.0)
account2 = st.number_input('Monthly Income from Account 2', value=0.0)
account3 = st.number_input('Monthly Income from Account 3', value=0.0)

# Calculate mean monthly income
mean_income = np.mean([account1, account2, account3])
st.session_state['mean_income'] = mean_income


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
st.session_state['net_worth'] = net_worth
# Display net worth
st.write(f'Net Worth: ${net_worth}')
