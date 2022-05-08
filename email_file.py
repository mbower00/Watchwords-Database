# used code from https://realpython.com/python-send-email/
import smtplib
import ssl
def email_file(file_to_send, receiver_email_address, sender_password):
    """Sends an email to the specified address with the contents of the specified file

    Args:
        file_to_send (str): the file with the contents to send
        receiver_email_address (str): receiver's email address (also, the subject of the email, sans ".txt")
        sender_password (str): password for mitchbbowercode@gmail.com
    """
    with open(file_to_send, "r") as the_file:
        mail = f"Subject: {file_to_send.replace('.txt', '')}\n\n"
        for i in the_file:
            mail = mail + i + "\n"
    
    with smtplib.SMTP_SSL("smtp.gmail.com", context=ssl.create_default_context()) as server:
        server.login("mitchbbowercode@gmail.com", sender_password)
        # receiver = input("Please enter the receiver email address > ")
        server.sendmail("mitchbbowercode@gmail.com", receiver_email_address, mail)