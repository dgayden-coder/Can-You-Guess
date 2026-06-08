import streamlit as st
import random
st.title("🎈 Can You Guess IT?")
st.subheader(
    "Let's see if you can guess the correct option"
)

if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1,50)


guess = st.number_input('input a number between 1-50',min_value=1, max_value=50, step=1)

if st.button('Submit Guess'):
    st.write('You guessed', str(guess))
    if guess < st.session_state.secret:
        st.warning('Sorry, too low!')
    elif guess > st.session_state.secret:
        st. warning('Sorry, too high!')
    else:
        st.success('Great Job! You Rock!')


if guess==st.session_state.secret:
    if st.button ('Play Again'):
        st.session_state.secret = random.randint (1,50)
        st.rerun()
    