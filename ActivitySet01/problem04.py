# Conditional Execution
hrs = input("enter hours:")
h = float(hrs)
rate=input("enter rate:")
rate=float(rate)
if h<=40 :
    pay = h*rate
else:
    pay= 40*rate + 1.5*rate*(h-40)
print(pay)
       
 
