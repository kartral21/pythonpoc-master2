import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import re
import json


class ATFEmail():
    def email_data(self):
        # account credentials
        username = "atftestaltran@gmail.com"
        password = "Test1234!"
        try:
            # create an IMAP4 class with SSL
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            # authenticate
            imap.login(username, password)
            status, messages = imap.select("INBOX")
            # number of top emails to fetch
            N = 3
            # tuple value
            json_list = []
            html_list = []
            # total number of emails
            messages = int(messages[0])
            for i in range(messages, messages-N, -1):
                # fetch the email message by ID
                res, msg = imap.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        # parse a bytes email into a message object
                        msg = email.message_from_bytes(response[1])
                        # decode the email subject
                        subject = decode_header(msg["Subject"])[0][0]
                        if isinstance(subject, bytes):
                            # if it's a bytes, decode to str
                            subject = subject.decode()
                        # email sender
                        from_ = msg.get("From")
                        print("Subject:", subject)
                        print("From:", from_)
                        # if the email message is multipart
                        if msg.is_multipart():
                            # iterate over email parts
                            for part in msg.walk():
                                # extract content type of email
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    # print text/plain emails and skip attachments
                                    slice_str = re.sub("\s*\d+\.\s+", "", body)
                                    try:
                                        final_json = json.loads(slice_str)
                                        print(final_json)
                                        for key in final_json.keys():
                                            print(final_json[key])
                                    except:
                                        print(slice_str)

                                elif "attachment" in content_disposition:
                                    # download attachment
                                    filename = part.get_filename()
                                    if filename:
                                        if not os.path.isdir(subject):
                                            # make a folder for this email (named after the subject)
                                            os.mkdir(subject)
                                        filepath = os.path.join(subject, filename)
                                        # download attachment and save it
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                        else:
                            # extract content type of email
                            content_type = msg.get_content_type()
                            # get the email body
                            body = msg.get_payload(decode=True).decode()
                            if content_type == "text/plain":
                                # print only text email parts
                                print(body)
                        if content_type == "text/html":
                            try:
                                reval = re.sub("<[\W\w]*?>", "", body)
                                reval1 = re.sub("\&quot\;", '"', reval)
                                reval2 = re.sub(" ", '', reval1)
                                final_json = json.loads(reval2)
                                json_tuple = (from_,subject,final_json)
                                json_list.append(json_tuple)
                                for key in final_json.keys():
                                    print(final_json[key])
                            except:
                                print(body)
                            html_list.append(body)
                        #     # if it's HTML, create a new HTML file and open it in browser
                        #     if not os.path.isdir(subject):
                        #         # make a folder for this email (named after the subject)
                        #         os.mkdir(subject)
                        #     filename = f"{subject[:50]}.html"
                        #     filepath = os.path.join(subject, filename)
                        #     # write the file
                        #     open(filepath, "w").write(body)
                        #     # open in the default browser
                        #     webbrowser.open(filepath)
                        print("="*100)
            imap.close()
            imap.logout()
            dict = {"json_list":json_list,"html":html_list[0]}
            return dict
        except Exception as e:
            raise e

if __name__ == "__main__":
    email = ATFEmail()
    email.email_data()
