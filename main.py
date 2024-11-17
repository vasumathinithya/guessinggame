import streamlit as st
import random

if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.random_number:
            st.write("Your guess is too low! Try again.")
        elif guess > st.session_state.random_number:
            st.write("Your guess is too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.write("New game started! Guess a new number.")

st.write(f"Number of attempts: {st.session_state.attempts}")
