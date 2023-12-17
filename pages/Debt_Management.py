import streamlit as st

st.title('Debt Management')

# Input fields for debts
mortgage = st.number_input('Mortgage', value=0.0)
student_loans = st.number_input('Student Loans', value=0.0)
credit_card_debt = st.number_input('Credit Card Debt', value=0.0)
other_debt = st.number_input('Other Debt', value=0.0)

# Calculate total debt
total_debt = mortgage + student_loans + credit_card_debt + other_debt
st.write(f'Total Debt: ${total_debt}')

# Input fields for debt payment plan
monthly_income = st.number_input('Monthly Income', value=0.0)
monthly_expenses = st.number_input('Monthly Expenses', value=0.0)
monthly_savings = st.number_input('Monthly Savings', value=0.0)

# Calculate available money for debt payment
available_money = monthly_income - monthly_expenses - monthly_savings

# Calculate months to pay off debt
months_to_pay_off_debt = total_debt / available_money if available_money > 0 else 0

st.write(f'Available Money for Debt Payment: ${available_money}')
st.write(f'Months to Pay Off Debt: {months_to_pay_off_debt}')