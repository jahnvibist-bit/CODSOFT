import random
import string
import math
passl=int(input("Enter lenght for ur password generation: "))
if passl<8:
    print("Entered length for password should be greater than 8 or exaxt 8 ! ")
else: 
    char=string.ascii_letters+string.digits
    passw="".join(random.choices(char,k=passl))
print("Your Password: ",passw)
