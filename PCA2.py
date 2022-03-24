from tkinter import *
import tkinter as tk
import os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile, askopenfilename


email_recipient = ""

r=tk.Tk(className='price change')

# setting the windows size
r.geometry("200x50")


# Create the body of the message (a plain-text and an HTML version).

content = """<pre> 
   Please find latest price change using link: <a href="https://bookworldzm.sharepoint.com/:f:/s/bookworldshared/Eg8YJV4i49FIpuAALGCZiLQBnQ9JHCSmOOPj3OyZ3MmC_g?e=6DafWT/">click here</a>\nPlease note the Prices will be adjusted in the next 10min
    </pre>"""



def send_email(email_recipient,
               email_subject,
               attachment_location = content):

    email_sender = 'it@bookworld.co.zm'

    #email_recipient = ["mandahill@bookworldzambia.com", "cairo@bookworldzambia.com", "kulima@bookworldzambia.com", "arcades@bookworldzambia.com", "kamloops@bookworldzambia.com", "pinnacle@bookworldzambia.com", "chipata@bookworldzambia.com", "solwezi@bookworldzambia.com", "mazabuka@bookworldzambia.com", "makeni@bookworldzambia.com", "ndola@bookworldzambia.com", "kitwe@bookworldzambia.com", "ridgeway@bookworldzambia.com", "crossroads@bookworldzambia.com", "janet@bookworld.co.zm", "itmanager@bookworld.co.zm", "stockcontroller@bookworld.co.zm", "areamanager@bookworldzambia.com", "warehouse1@bookworldzambia.com"]
    email_recipient = ["maingamiyanda3@gmail.com", "maingamiyanda3@outlook.com"]


    msg = MIMEMultipart('alternative')
    msg['From'] = email_sender
    msg['To'] = ",".join(email_recipient)
    msg['Subject'] = email_subject

    # Record the MIME types of both parts - text/plain and text/html.

    part2 = MIMEText(content,'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.

    msg.attach(part2)


    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login('it@bookworld.co.zm', 'Suw733444')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True


# defining a function that will
# get the memo and
# send an email
def submit():


    send_email(email_recipient,
               'Price Change',
               content)


# creating a label forz
# memo using widget Label
memo_label = tk.Label(r, text = 'Sharepoint Link',
                      font=('calibre',
                            10,'italic'))


# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(r,text = 'Submit',
                  command = submit)

# placing the label and entry in
# the required position using grid
# method

sub_btn.grid(row=1,column=2)


# performing an infinite loop
# for the window to display
r.mainloop()
