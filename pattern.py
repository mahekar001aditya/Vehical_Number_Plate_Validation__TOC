import re

p= (r'^{A-Z}{2},{0-9}{2},{A-Z}{1,2},{0-9}{4}$')
num=input("enter number:")
if re.match(p,num):
  print("number is valid")
else:
  print("number is not valid")