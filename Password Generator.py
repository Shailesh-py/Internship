import random
import string

length = int(input("Enter the Desired Length of Password : "))
print("".join(random.choices(string.ascii_letters + string.digits, k=length)))
