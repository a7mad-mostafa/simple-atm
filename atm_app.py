import streamlit as st


st.markdown(
    """
    <h1 style='text-align: center; color: #99004d; font-family: cursive;' > Welcome to ATM App! </h1>
    """,
    unsafe_allow_html=True
)

st.markdown( """
    <div style="display: flex; justify-content: center;">
        <img src="https://www.atmofamerica.com/wp-content/uploads/2016/06/6172535_G.jpg" width="400" style="border-radius: 30px;">
    </div>
    """,unsafe_allow_html=True)


if 'balance' not in st.session_state:
    st.session_state.balance = 0

ch1 = '1. Deposit Money'
ch2 = '2. Withdraw Money'
ch3 = '3. Check Balance'
ch4 = '4. Exit'

def deposit_money():
    amount = st.number_input('Enter the amount to deposit: ')
    if st.button('Deposit'):
        st.session_state.balance += amount
        st.success(f'### You have successfully deposited ${amount}')

def withdraw_money():
    amount = st.number_input('Enter the amount to withdraw: ')
    if st.button('Withdraw'):
        if amount > st.session_state.balance:
            st.error('### Insufficient balance!')
            return
        else:
            st.session_state.balance -= amount
            st.warning(f' ### You have successfully withdrawn ${amount}')

def check_balance():
    st.info(f' ### Your current balance is ${st.session_state.balance}')

st.write(' ')
st.write('# Choose the operation: ')
choice = st.radio(' ', [ch1,ch2,ch3,ch4])

if choice == ch1:
    deposit_money()
elif choice == ch2:
    withdraw_money()
elif choice == ch3:
    check_balance()
else:
    st.info('### Goodbye!')
    