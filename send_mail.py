import pandas as pd
from emailer import Emailer

data = pd.read_csv('data.csv', delimiter=';')
with open('mail_text.txt') as f:
    text = f.read()

subject = ''
for i in range(len(data)):
    message = 'Dear ' + data.name[i] + '<br><br>' + text
    Emailer(message, subject, data.mail[i])