import imaplib
import email
import traceback 
import string
# from credentials import FROM_EMAIL,FROM_PWD
FROM_EMAIL = "mayurdabade1103@gmail.com"
FROM_PWD = "psgn snfk ljee asxq" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

from bs4 import BeautifulSoup

def decode_subject(encoded_subject):
    try:
        decoded_subject = email.header.decode_header(encoded_subject)[0][0]
        if isinstance(decoded_subject, bytes):
            return decoded_subject.decode()
        elif isinstance(decoded_subject, str):
            return decoded_subject
        else:
            return encoded_subject
    except Exception as e:
        print(f"Error decoding subject: {str(e)}")
        return encoded_subject

def remove_non_printable(text):
    printable = set(string.printable)
    return ''.join(filter(lambda x: x in printable, text))

def read_email_from_gmail(n):
    try:
        with open("emails.txt", "w", encoding="utf-8") as file:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL, FROM_PWD)
            mail.select('inbox')

            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()
            # Limit the number of emails to fetch to the latest 10
            latest_email_id = int(id_list[-1])
            first_email_id = max(1, latest_email_id - n)  # Fetch latest 10 emails
            for i in range(latest_email_id, first_email_id - 1, -1):
                data = mail.fetch(str(i), '(RFC822)')
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_bytes(arr[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        file.write('From : ' + email_from + "\n")
                        decoded_subject = decode_subject(email_subject)
                        file.write('Subject : ' + decoded_subject + "\n")
                        for part in msg.walk():
                            if part.get_content_type() == "text/html":
                                # Parse HTML content using BeautifulSoup
                                soup = BeautifulSoup(part.get_payload(decode=True).decode('utf-8'), 'html.parser')
                                # Extract text from HTML and remove leading/trailing whitespace
                                email_content = "\n".join(line.strip() for line in soup.get_text(separator="\n").splitlines() if line.strip())
                                email_content_cleaned = remove_non_printable(email_content)
                                file.write("Content :\n" + email_content_cleaned + "\n")
                                file.write("-" * 30 + "\n")
    except Exception as e:
        traceback.print_exc()
        print(str(e))


def read_gmail_subjects(num):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        latest_email_id = int(id_list[-1])
        first_email_id = max(1, latest_email_id - num + 1)  # Fetch the latest 'num' emails
        subjects = []

        for i in range(latest_email_id, first_email_id - 1, -1):
            data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_bytes(arr[1])
                    email_subject = msg['subject']
                    decoded_subject = decode_subject(email_subject)
                    subjects.append(decoded_subject)

        # Display subjects with numbers
        formatted_subjects = [f"{idx}. {subject}" for idx, subject in enumerate(subjects, 1)]
        return formatted_subjects
    except Exception as e:
        traceback.print_exc()
        print(str(e))


# read_gmail_subjects()



# read_email_from_gmail()
