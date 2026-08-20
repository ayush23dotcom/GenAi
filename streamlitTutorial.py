import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello User")

name = st.text_input("Enter your name")

if st.button("Greet"):
    st.success(f"Hello, {name}")

upload_file = st.file_uploader("Upload a CSV", type="csv")

if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

    st.header("This is my first project")
    st.subheader("This is the work I done")

    st.markdown("[Link](https://streamlit.io/)")

    st.text_area("Write your message")

    st.number_input("Pick a number", min_value=0, max_value=10)

    st.slider("Choose a range", 0, 100)

    st.selectbox(
        "Select a fruit",
        ["apple", "banana", "mango"]
    )

    st.multiselect(
        "Select language",
        ["java", "python", "c", "c++"]
    )

    st.radio(
        "Pick one",
        ["Option A", "Option B"]
    )

    st.checkbox("I agree to the terms and conditions")

    if st.checkbox("Show details"):
        st.info("Here are more details")

    # Login Form
    with st.form("Login form"):

        username = st.text_input("Enter username")

        password = st.text_input(
            "Password",
            type="password"
        )

        submitted = st.form_submit_button("Login")

        if submitted:
            st.success(f"Welcome, {username}!")

    # Forgot Password
    st.write("")

    if st.button("Forgot Password?"):

        st.subheader("Reset Password")

        email = st.text_input(
            "Enter your email address"
        )

        if st.button("Send Reset Link"):

            if email:
                st.success(
                    f"Password reset link sent to {email}"
                )
            else:
                st.warning(
                    "Please enter your email address."
                )
    df = pd.DataFrame(np.random.randn(20,3), columns=["A","B","C"])
    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)
    st.video("https://youtu.be/1Tdy3JshqCs?si=0dlwEUT1QrptRKQO")
    st.image( "https://static.vecteezy.com/system/resources/thumbnails/057/068/323/small/single-fresh-red-strawberry-on-table-green-background-food-fruit-sweet-macro-juicy-plant-image-photo.jpg",caption="My Image")
    