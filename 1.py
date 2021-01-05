import re
import csv
import os

#Email Masker

def emask(email):
    result = re.sub(r"@[\w.-]+", "[HIDDEN]", email)
    return(result)

#Phone Masker

def pmask(phone):
#    result = re.sub(r"\(\d{3}\)+\d{3}\-", r"[HIDDEN]", phone)
    result = "[HIDDEN]" + ''.join(re.findall(r"\d", phone))[-4:]
    return(result)

#z = [["Name:",name,"Email:",email,"Phone:",phone]]
z= list()

#Powershell Display

x = open("path.txt")
csv_x = csv.reader(x)
for row in csv_x:
    name, email, phone = row
    email = emask(email)
    phone = pmask(phone)
    print("Name: {:>14} | Email: {:>22} | Phone: {:>}".format(name, email, phone))
    z.append(["Name:",name,"Email:",email,"Phone:",phone])

#CSV File Output

with open("path.csv", "w") as list_csv:
    writer = csv.writer(list_csv)
    writer.writerows(z)