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

memo = ""
con = ""
content = ""
email_recipient = ""

r=tk.Tk(className='price change')

# setting the windows size
r.geometry("300x100")

# declaring string variable
# for storing memo number
memo_var=tk.StringVar()

def open_file():
    file = askopenfilename(initialdir="/", filetypes=[('all files', "*.*")])
    if file is not None:
        global content
        con = file
        content = con

    # list of reciver email_id to the mail
    #li = ["maingamiyanda3@outlook.com", "maingamiyanda3@gmail.com", "katongopython2020@gmail.com",  ]


    # getting length of list
    #length = len(li)

    # Iterating the index
    # same as 'for i in range(len(list))'

    # Here we iterate the loop and send msg one by one to the reciver
    #for i in range(length):
       # X = li[i]
       # email_recipient = X

        #print(email_recipient)


def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location = content):

    email_sender = 'it@bookworld.co.zm'

    #email_recipient = ["maingamiyanda3@outlook.com", "maingamiyanda3@gmail.com", "katongopython2020@gmail.com", "onganip@gmail.com"]
    email_recipient = ["itadmin@bookworld.co.zm", "maingamiyanda3@gmail.com", "itmanager@bookworld.co.zm"]


    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = ",".join(email_recipient)
    msg['Subject'] = email_subject


    msg.attach(MIMEText(email_message,'plain'))

    if attachment_location == content:
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "content; filename= %s" % filename)
        msg.attach(part)
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
    global memo
    mem = memo
    mem = memo_entry.get()


    send_email(email_recipient,
               'Price Change',
               'Please find attached price change memo number ' + mem,
                content)

    #print("Please " + mem)

    memo_var.set("")

# creating a label for
# memo using widget Label
memo_label = tk.Label(r, text = 'memo number',
                      font=('calibre',
                            10, 'italic'))

# creating a entry for input
# memo using widget Entry
memo_entry = tk.Entry(r,
                      textvariable = memo_var,
                      font=('italic',10,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(r,text = 'Submit',
                  command = submit)

# placing the label and entry in
# the required position using grid
# method
memo_label.grid(row=0,column=0)
memo_entry.grid(row=0,column=1)

sub_btn.grid(row=3,column=1)


btn = tk.Button(r, text ='Open', command = lambda:open_file())


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns


btn.grid(column=1, row=2)



# performing an infinite loop
# for the window to display
r.mainloop()
