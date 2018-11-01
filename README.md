# SecretSanta
A program to randomly distribute Secret Santa selection

Classic Secret Santa explained: https://www.dictionary.com/browse/secret-santa

## Why I made this program
Current methods' problems:
* Names from a hat: everyone has to be together at the same time
* One person making the pairs: they can't participate
* Online sites: they don't handle exceptions/rules

My family wants to do a Secret Santa Exchage instead of our tradition 'everyone buys a gift for everyone'. We won't be all together until around Christmas time since we all have our own families and live in different cities. Also, there's no way we're not getting our immediate family members presents anyway, so we don't want to 'pull' their names. I'm willing to do upfront work, but I want to participate as well. 

## Requirements
* Python 3.7 (not tested on previous version)
* Edited CSV file
* SMTP mail server  
   If you're using Gmail, use option 2 here: https://support.google.com/accounts/answer/6010255
    
 ## Use
Download both files (SecretSanta.py and SantaRules.csv) and place them in the same folder. Start by editing the csv in a text editor or excel. Add the email address of each Santa in the first column of each row (skipping the first for column headers).  Add their real name in the last column of their row (not required). 

The headers are the gift getters names. You can list these headers in any order, but I suggest ordering them left to right the same as they are ordered in the first column top to bottom. If you're using excel, you can copy the last column's cells and paste them 'transposed' in the second column first row to get the headers.  

Now fill in the data, placing 0 (zero) where the Santa on row shouldn't have the gift getter in the column selected for them.  Place 1 (one) where its allowed. 

Run SecretSanta.py, and enter the email address and password of the account you want the notificaiton email sent from. 

If there is an error, it will print to the screen and won't send the emails.  Try running again. It's posible that your rules have made it so there are no or a very low number of good complete solutions. Each run will only try one posible solution.
