from Tkinter import *
import tkMessageBox
import getpass, imaplib
import quopri

class App:
    
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        self.run = Button(frame, text="GetIt!", command=self.work, padx=10, pady=10)
        self.run.pack(padx=20, pady=20)
        self.run.config(cursor='gumby')
        self.run.config(bd=8, relief=RAISED)
        self.run.config(bg='dark green', fg='white')
        self.run.config(font=('helvetica', 20, 'underline italic'))
        
        
    def work(self):
        M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        M.login('yourmail@gmail.com', 'password')
        M.select()
        typ, data = M.search(None, '(BODY "Select Your Events")')
        f = open('fest.txt', 'w')
        for num in data[0].split():
            f.close()
            f = open('fest.txt', 'r+')
            typ, data = M.fetch(num, '(RFC822)')
            message = 'Message %s\n%s\n' % (num, data[0][1])
            index =  message.find('Name')
            last = message.find('Sender IP')
            atlast = message[index:last-40]
            atleast = quopri.decodestring(atlast)
            already = f.read()
            if atlast not in already:
                f.close()
                f = open('fest.txt', 'a+')
                f.write(atlast)
                f.write('------------------------------------------------------\n\n')
        tkMessageBox.showinfo("Done!", "Done!")
        M.close()
        M.logout()
    
root = Tk()

app = App(root)
root.mainloop()