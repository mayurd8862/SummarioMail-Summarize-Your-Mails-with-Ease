
import streamlit as st
from main import *
from langchain.llms import GooglePalm

st.title("💬🚀Mails Summarizer", divider='rainbow')
num = st.number_input("Enter the number of Emails You want to summarize:", min_value=1, step=1)
if st.button("Summarize"):
    read_email_from_gmail(num)  # Convert num to integer before passing to function
    st.write(f"Summary of first {num} documents are as follows:")
    st.write(output)

















