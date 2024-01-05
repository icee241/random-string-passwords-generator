import random
 
print("-------------------------")
print("WARNING, max length is 99")
print("-------------------------")
l1=input("Enter Lenght")






lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]|@#¢∞¬÷“”≠œæ€®†¥  øπ~§¶™∂∫å∑©√µ„…–"

string= lower + upper + numbers +symbols
length= int(l1)
password="".join(random.sample(string, length))
print("-------------------------")
print("Your safe password is:" + password)
print("-------------------------")
