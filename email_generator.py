import random
import time
txt = 'EMAIL GENERATOR'
cent = txt.center(130)
print("\n",cent)

time.sleep(0.5)

name = input("\nEnter your Name: ")

fn = name.lower()

numb = '1234567890'


char = '@'

dmn = input("enter the domain name: ")
domain = dmn.lower()
tdmn = input("enter the domain (for eg:.com,.ord,.edu) : ")

var = 1
el = 3

for i in range(var):
    eml = ''
    for j in range(el):
        eml += random.choice(fn)
        
nu = random.choice(numb)

lst = [eml,nu,char,domain,tdmn]

email = "".join(lst)
print(email)