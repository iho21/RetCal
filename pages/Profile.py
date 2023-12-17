import streamlit as st

st.title('Financial Dashboard')
st.subheader('A simple financial dashboard to track your income, expenses, savings, and investments.')
st.caption("Enter your income, expenses, savings, and investments to see your financial metrics in sidebar")
# Sidebar for user inputs
with st.sidebar:
    st.header('User Inputs')
    income = st.number_input('Monthly Income', value=0.0)
    expenses = st.number_input('Monthly Expenses', value=0)
    savings = st.number_input('Monthly Savings', value=0.0)
    investments = st.number_input('Investments', value=0.0)

# Calculate financial metrics
net_income = income - expenses
savings_rate = (savings / income) * 100 if income > 0 else 0
investment_return = investments * 0.07  # Assuming a 7% annual return on investments

# Display financial metrics
st.header('Financial Metrics')
st.metric('Net Income', f'${net_income}', delta='0')
st.metric('Savings Rate', f'{savings_rate}%', delta='0')
st.metric('Estimated Annual Return on Investments', f'${investment_return}', delta='0')

# Display financial overview
st.header('Financial Overview')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Income')
    st.bar_chart({'Income': [income]})
with col2:
    st.subheader('Expenses')
    st.bar_chart({'Expenses': [expenses]})

# Display savings and investments
st.header('Savings and Investments')
col1, col2 = st.columns(2)
with col1:
    st.subheader('Savings')
    st.bar_chart({'Savings': [savings]})
with col2:
    st.subheader('Investments')
    st.bar_chart({'Investments': [investments]})