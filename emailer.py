def Emailer(message, subject, recipient, **kwargs):
    import win32com.client as win32   

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    for arg in kwargs:
        if arg == 'sender':
            mail.SentOnBehalfOfName = kwargs[arg]
        if arg == 'cc':
            mail.CC = kwargs[arg]
    mail.To = recipient
    mail.Subject = subject
    mail.GetInspector

    index = mail.HTMLBody.find('>', mail.HTMLBody.find('<body')) 
    mail.HTMLBody = mail.HTMLBody[:index + 1] + message + mail.HTMLBody[index + 1:] 

    mail.Display(False)
    mail.Send() #uncomment if you want to send instead of displaying
    
if __name__ == '__main__':
    Emailer('hej', 'tejgfeoijgoiewrugst', 'solha@byg.dtu.dk')