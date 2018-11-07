#! python3

import csv
import random
import time
import smtplib

timeout = 5

class Santa:
    def __init__(self, data):
        self.email = data[0]                #Secret Santa's email address
        self.name = data[len(data)-1]       #Secret Santa's real name
        self.rules = data[1:(len(data)-1)]  #Py Dictionary of 1's and 0's (1 = allowed santee, 0=disallowed)
        self.santee = ''                    #Santee is the person recieving this Secret Santa's gift
        self.convert()

    def convert(self): #Changes the rules from 1's and 0's to boolean values
        for i in range(len(self.rules)):
            if self.rules[i] == '1':
                self.rules[i] = True
            else:
                self.rules[i] = False
        
    def print(self): #prints this class for debugging purposes
        print(self.name)
        print(self.email)
        print(self.rules)
        print(self.santee)

    def update(self, column, value): #not used
        self.rules[column] = value

    def toggle(self, column): #not used
        self.rules[column] = not self.rules[column]

    def randChoice(self): #randomly selects one of the allowed (true) values from 'rules' and returns it's position
        now = round(time.time())
        randColumn = 0
        while randColumn <= 0:
            randColumn = random.randint(1,(len(self.rules)))
            if self.rules[randColumn-1]:
                return randColumn
            else:
                randColumn = 0
                if round(time.time()) - now > timeout:
                    print("timeout in randChoice")
                    errorHappened = True
                    break

#Read in a CSV with:
    #first column Secret Santa email addresses,
    #last column Secret Santa real names,
    #column headers are real names (above transposed),
    #data as 1's and 0's
santaFile = open('SantaRules.csv')
santaReader = csv.reader(santaFile)
santaData = list(santaReader)

#Create list of all Secret Santas from csv
santas = []
headers = []
firstRow = True
for row in santaData:
    if firstRow:
        headers = row
        firstRow = False
    else:
        newSanta = Santa(row)
        santas.append(newSanta)

#Randomly select all Secret Santa's recipients (santee)
prevSelected = []
errorHappened = False
for santa in santas:
    now = round(time.time()) #start watachdog
    selected = 0
    while selected <= 0:
        selected = santa.randChoice() #get a random column
        if selected not in prevSelected: #check if column was already selected by different santa
            prevSelected.append(selected)
            prevSelected.sort()
        else:
            selected = 0 #repeat until random choice is a column no other previous Santa recieved
            if round(time.time()) - now > timeout: #watchdog expried, no posible choice exists for this Santa
                print("timeout in main loop")
                errorHappened = True
                break
    santa.santee = headers[selected]
#    print(santa.name+" - "+santa.santee) #prints list for debugging purposes

#Send out emails to all Secret Santas
email = input('Enter your email address: ')
password = input('Enter your email password: ')
if not errorHappened:
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login(email, password)
    for santa in santas:
#        remove comment on next line to enable emails
#        s.sendmail(email, santa.email, 'Subject: Secret Santa\nDear '+santa.name+', you are Santa this year for '+santa.santee+'. Shhh...its a secret')
    s.quit()
