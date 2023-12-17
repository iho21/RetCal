import streamlit as st

st.title('Expense Planning')

# Input fields for monthly expenses
housing = st.number_input('Housing', value=0.0)
utilities = st.number_input('Utilities', value=0.0)
groceries = st.number_input('Groceries', value=0.0)
insurance = st.number_input('Insurance', value=0.0)
other_expenses = st.number_input('Other Expenses', value=0.0)

# Calculate total monthly and annual expenses
total_monthly_expenses = housing + utilities + groceries + insurance + other_expenses
total_annual_expenses = total_monthly_expenses * 12

st.write(f'Total Monthly Expenses: ${total_monthly_expenses}')
st.write(f'Total Annual Expenses: ${total_annual_expenses}')

# Input fields for retirement planning
years_to_retirement = st.number_input("Years to retire")
interest = st.number_input("Interest rate")
principal = st.number_input("Principal amount")

# Calculate retirement savings
result = principal * pow(1 + interest / 100, years_to_retirement) - total_annual_expenses * years_to_retirement

if st.button("Calculate"):
    st.write(f'You will have ${result} at retirement after expenses.')