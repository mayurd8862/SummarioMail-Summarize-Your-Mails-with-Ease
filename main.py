import imaplib
import email
import traceback 

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import GooglePalm

api_key = 'AIzaSyDoi9dYBVNne75DD4P-pce6Pf3i-Ol7Cbo'

llm = GooglePalm(google_api_key=api_key, temperature=0.1)

FROM_EMAIL = "mayurdabade1103@gmail.com"
FROM_PWD = "psgn snfk ljee asxq" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

from bs4 import BeautifulSoup

import imaplib
import email
import traceback 

FROM_EMAIL = "mayurdabade1103@gmail.com"
FROM_PWD = "psgn snfk ljee asxq" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

from bs4 import BeautifulSoup

def read_email_from_gmail(num):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        # Limit the number of emails to fetch to the latest 10
        latest_email_id = int(id_list[-1])
        first_email_id = max(1, latest_email_id - (num-1))  # Fetch latest 10 emails
        with open("emails.txt", "w", encoding="utf-8") as file:
            for i in range(latest_email_id, first_email_id - 1, -1):
                data = mail.fetch(str(i), '(RFC822)')
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_bytes(arr[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        file.write('From : ' + email_from + "\n")
                        file.write('Subject : ' + email_subject + "\n")
                        for part in msg.walk():
                            if part.get_content_type() == "text/html":
                                # Parse HTML content using BeautifulSoup
                                soup = BeautifulSoup(part.get_payload(decode=True).decode('utf-8'), 'html.parser')
                                # Extract text from HTML and remove leading/trailing whitespace
                                email_content = "\n".join(line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip())
                                file.write("Content :\n" + email_content + "\n")
                                file.write("-" * 30 + "\n")
    except Exception as e:
        traceback.print_exc()
        print(str(e))

# read_email_from_gmail()




paul_graham_essay = 'emails.txt'

with open(paul_graham_essay, 'r',encoding="utf-8") as file:
    essay = file.read()

# tokens = llm.get_num_tokens(essay)

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=1000, chunk_overlap=100)

docs = text_splitter.create_documents([essay])

summary_chain = load_summarize_chain(llm=llm, chain_type='map_reduce',
                                    #  verbose=True 
                                    )

output = summary_chain.run(docs)

# if __name__ == "__main__":
#     read_email_from_gmail(1)