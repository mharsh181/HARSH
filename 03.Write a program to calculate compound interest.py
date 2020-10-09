#Write a program to calculate compound interest.
#input
p=eval(input("Enter the principal amount : "))
r=eval(input("Enter the rate of interest : "))
t=eval(input("Enter the time in years : "))

#calculations
x=(1+r/100)**t
CI= p*x-p

#output
print("Compound interest is : ", round(CI,2))