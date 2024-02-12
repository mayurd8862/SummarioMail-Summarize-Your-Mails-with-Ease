a = """
🤷‍♂️How to get gmail API password??

1. 📧 Make sure you enable IMAP in your Gmail settings. (Log on to your Gmail account and go to Settings ⚙️, See All Settings, and select Forwarding and POP/IMAP tab. In the "IMAP access" section, select Enable IMAP.)

2. If you have 2-factor authentication, Gmail requires you to create an application-specific password that you need to use. Go to your Google account settings and click on 'Security'. Scroll down to App Passwords under 2-step verification. Select Mail under Select App 📬 and Other under Select Device 📱. (Give a name, e.g., python) The system gives you a password that you need to use to authenticate from Python. 🔑

"""

import streamlit as st
from fetch_mails import read_email_from_gmail, read_gmail_subjects
from summarize import *

st.title("💬🚀SummarioMail: Summarize Your Mails with Ease")

mail = st.text_input("Enter Your Mail:")
api_pwd = st.text_input("Enter Your API password:",type='password')
st.write(a)

submit = st.checkbox('Submit details')
# st.write()

if submit:
    # st.write(mail)
    # st.write(api_pwd)

    st.write('______________\n ')
    num = st.slider("✔️Select the number of emails you want to fetch", min_value=1, max_value=10, value=3, step=1)
    read_email_from_gmail(num)
    subjects = read_gmail_subjects(num)
    st.write(f"Subjects of latest {num} emails:")
    for subject in subjects:
        st.write(subject)
    



    st.write('______________\n ')
    num2 = st.number_input("✔️Enter count no of mail U wanna summarize:", min_value=1, step=1)

    if st.button("Summarize"):
        summary_output = summary(num2)
        st.write(summary_output)





# import streamlit as st
# from fetch_mails import read_email_from_gmail, read_gmail_subjects
# from summarize import *

# st.title("💬🚀SummarioMail: Summarize Your Mails with Ease")

# def save_credentials(mail, api_pwd):
#     with open("credentials.py", "w") as file:
#         file.write(f"FROM_EMAIL='{mail}'\nFROM_PWD='{api_pwd}'")

# mail = st.text_input("Enter Your Mail:")
# api_pwd = st.text_input("Enter Your API password:", type='password')

# submit = st.checkbox('Submit details')

# if submit:
#     save_credentials(mail, api_pwd)
#     st.write('Credentials saved successfully!')

#     num = st.slider("Select the number of emails you want to fetch", min_value=1, max_value=10, value=3, step=1)
#     read_email_from_gmail(num)
#     subjects = read_gmail_subjects(num)
#     st.write(f"Subjects of first {num} emails:")
#     for subject in subjects:
#         st.write(subject)

#     st.write('______________\n ')
#     num2 = st.number_input("Enter count no of mail U wanna summarize:", min_value=1, step=1)

#     if st.button("Summarize"):
#         summary_output = summary(num2)
#         st.write(summary_output)
